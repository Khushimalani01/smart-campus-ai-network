import numpy as np, pandas as pd
from sklearn.ensemble import RandomForestRegressor, IsolationForest
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, precision_score, recall_score

# 1. Simulate 60 days of hourly campus traffic
rng = np.random.default_rng(42)
t = np.arange(24 * 60)
hour, dow = t % 24, (t // 24) % 7
users = 200 + 150 * np.exp(-((hour - 14) ** 2) / 18)
users = users * np.where(dow >= 5, 0.5, 1.0) + rng.normal(0, 15, t.size)
users = np.clip(users, 5, None)
bw = 1.8 * users + rng.normal(0, 20, t.size)          # bandwidth in Mbps
anom = np.zeros(t.size, dtype=int)
for i in rng.choice(t.size, 24, replace=False):       # abnormal spikes
    bw[i] *= rng.uniform(1.8, 2.6)
    anom[i] = 1

# 2. Build features (lagged values) and split by time
df = pd.DataFrame({"hour": hour, "dow": dow, "users": users,
                   "bw": bw, "anom": anom})
df["bw_lag1"] = df.bw.shift(1)
df["bw_lag24"] = df.bw.shift(24)
df["users_lag1"] = df.users.shift(1)
df = df.dropna().reset_index(drop=True)
cut = int(len(df) * 0.75)
train, test = df.iloc[:cut], df.iloc[cut:]
X = ["hour", "dow", "bw_lag1", "bw_lag24", "users_lag1"]

# 3. Traffic prediction: Random Forest vs Linear Regression baseline
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(train[X], train.bw)
lr = LinearRegression().fit(train[X], train.bw)
print("RF MAE :", mean_absolute_error(test.bw, rf.predict(test[X])))
print("LR MAE :", mean_absolute_error(test.bw, lr.predict(test[X])))

# 4. Anomaly detection: Isolation Forest on users and bandwidth
iso = IsolationForest(contamination=0.03, random_state=42)
iso.fit(train[["users", "bw"]])
flag = (iso.predict(test[["users", "bw"]]) == -1).astype(int)
print("Precision:", precision_score(test.anom, flag))
print("Recall   :", recall_score(test.anom, flag))

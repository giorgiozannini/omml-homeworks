import bonus as f
import pandas as pd

# splitting data
data = pd.read_excel('dataPoints.xlsx')
X_train, X_test, y_train, y_test = f.data_split(data)

# running the optimizer
N = 128; sigma = 6.5; rho = 1e-5; method = "BFGS";

nn = f.two_blocks(X_train, y_train,X_test, y_test, N = N, sigma = sigma, rho = rho, method = method)
nn.optimize()

data = pd.read_excel('dataPointsTest.xlsx.')
X_newtest, y_newtest = f.test_split(data)
y_pred = nn.predict(X_newtest, nn.w, nn.b, nn.v)

print("test error :", f.test_mse(y_pred, y_newtest))
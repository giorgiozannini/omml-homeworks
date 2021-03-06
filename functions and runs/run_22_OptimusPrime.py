import rbf_2 as f
import pandas as pd

# splitting data
data = pd.read_excel('dataPoints.xlsx')
X_train, X_test, X_val, y_train, y_test, y_val  = f.data_split(data)

# running the optimizer
N = 30; sigma = 0.5; rho = 1e-5; method = "BFGS"; seed = 361058965

nn = f.Rbf_el(X_train, y_train, N = N, sigma = sigma, rho = rho, method = method, seed = seed)
nfev, njev, time_elapsed = nn.optimize()

print("N :", N, "\nsigma :", sigma, "\nrho :", rho, "\nseed :", seed, "\nmethod :", method)
print("# of fun eval :", nfev, "\n# of grad eval :" , njev, "\ntime elapsed :", time_elapsed)
print("training error :", nn.mse(X_train, y_train, nn.c, nn.v))
print("test error :", nn.mse(X_test, y_test, nn.c, nn.v))
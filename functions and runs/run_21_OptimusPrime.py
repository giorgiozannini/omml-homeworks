import mlp_2 as f
import pandas as pd

# splitting data
data = pd.read_excel('dataPoints.xlsx')
X_train, X_test, X_val, y_train, y_test, y_val  = f.data_split(data)

# running the optimizer
N = 35; sigma = 8; rho = 1e-5; method = "BFGS"; seed = 630940773

nn = f.Mlp_el(X_train, y_train, N = N, sigma = sigma, rho = rho, method = method)
nfev, njev, time_elapsed = nn.optimize()

print("N :", N, "\nsigma :", sigma, "\nrho :", rho, "\nseed :", seed)
print("# of fun eval :", nfev, "\n# of grad eval :" , njev, "\ntime elapsed :", time_elapsed)
print("training error :", nn.mse(X_train, y_train, nn.w,nn.b, nn.v))
print("test error :", nn.mse(X_test, y_test, nn.w,nn.b, nn.v))
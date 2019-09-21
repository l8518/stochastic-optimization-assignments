
import numpy as np
import pandas as pd

class RevenueManagementDPSolver:
    """ This class answers the task 1) """

    y = (500, 300, 200)
    C = 5
    T = 10
    alpha = (0.001, 0.015, 0.05)
    beta = (0.01, 0.005, 0.0025)

    def f_lambda(self, t, i):
        return self.alpha[i] * np.exp(self.beta[i] * t)

    def f_V(self, t, x):
        if (not pd.isna(self.df[t][x])):
            return self.df[t][x]
        if (t == self.T):
            return 0
        if (x == 0):
            return 0
        n = len(self.y)
        max_value = [0]
        for j in range(n):
            # summing loop 1
            sum_1 = 0
            for i in range(j + 1):
                lambda_value = self.f_lambda(t, 1)
                subterm_1 = self.y[j] * self.f_V(t + 1, x - 1)
                sum_1 += lambda_value * subterm_1
            subsum_2 = 0
            for i in range(j + 1):
                lambda_value = self.f_lambda(t, 1)
                subsum_2 += lambda_value
            sum_2 = (1 - subsum_2) * self.f_V(t + 1, x)
            max_value.append( sum_1 + sum_2 )
        return max(max_value)

    def solve(self):
        self.df = pd.DataFrame(None, index=range(self.C + 1), columns=range(self.T + 1))
        print(self.df)
        for t in reversed(range(self.T + 1)):
            for small_c in range(self.C + 1):
                result = self.f_V(t, small_c)
                self.df[t][small_c] = result
        return self.df




                  

if __name__ == "__main__":
    rmdp = RevenueManagementDPSolver()
    df = rmdp.solve()
    print(df)

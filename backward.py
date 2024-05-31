from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import numpy as np 

def backward_elimination(df, dependent_value):
    # split the dataframe into dependent and independent variables.  
    x = df.drop([dependent_value], axis=1)
    y = df[dependent_value] 

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0) 
    
    lm = LinearRegression() 
    lm.fit(x_train, y_train) 
    pred = lm.predict(x_test) 

    import statsmodels.regression.linear_model as sm 


    x = np.append(arr = np.ones((1552, 1)).astype(int),  
                values = x, axis = 1) 

    x_opt = x
    ols = sm.OLS(endog = y, exog = x_opt).fit() 
    ols.summary() 

    for i in range(x.shape[1]):
        ols = sm.OLS(endog=y, exog=x_opt).fit()
        max_p_value = ols.pvalues.max()
        if max_p_value > 0.05: 
            max_p_idx = np.argmax(ols.pvalues)  
            x_opt = np.delete(x_opt, max_p_idx, axis=1)  
        else:
            break  

    ols = sm.OLS(endog=y, exog=x_opt).fit()
    print(ols.summary())
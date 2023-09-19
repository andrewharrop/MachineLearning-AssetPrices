With textual analysis, financial data (and accessability) are now on the "too much" side regarding the amount of information extractable. 

Suppose we have N=5000 securities, and J return covariates. The dimension of J could exceed N's cardinality. Even with rigorous regularization, tens or hundreds of features could still remain.

Conventional algorithams are not designed for this. If J>N in OLS regression, there will not be a unique solution. The historical solution has been to reduce J to a fraction of what is available. Sparsity is easy to work with, models behave well and are easy to understand. However, an abundance of data means that these handpicked features may have zero effect. Not everything is important, but academic literature has moved from three to six features in the past 30 years, which can be interpreted as an admission that relavant features are being omitted. 

Machine Learning is suitable for larger inputs. Take for example an image processing problem. There may be 500 64x64 images in a training set, but with machine learning, a robust model to classify these images can be produced. 

In asset pricing, knowledge about the properties of asset prices must be applied when selecting an algoritham. 

Ridge regression penalizes large coefficients. The derivation is similar to linear regression but contains an additional squared coefficient penalty in the minimization function. A hyperparameter γ controls the strength of the penalization.

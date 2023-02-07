def mean_absolute_percentage_error(y_true, y_pred):
    """     
    Mean Absolute Percentage Error,
    https://en.wikipedia.org/wiki/Mean_absolute_percentage_error for details    .
    """
    return np.mean(np.abs((np.asarray(y_true) - np.asarray(y_pred)) / np.asa    rray(y_true))) * 100

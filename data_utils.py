#08/08/2019
import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, f1_score, recall_score, accuracy_score

def csv_to_numpy_array(train_path, test_path):
	print("Loading training data...")
	traindata = pd.read_csv(train_path, header= None, delim_whitespace=True).values
	print("Train data loaded successfully!\n")
	#traindata = np.genfromtxt(train_path, dtype=None)
	
	print("Loading test data...")
	testdata = pd.read_csv(test_path, header= None, delim_whitespace=True).values
	print("Test data loaded successfully!\n")
	#testdata = np.genfromtxt(test_path, dtype=None)

	return transform_data(traindata, testdata)

def transform_data(x_train, x_test):
	[trainX, trainY] = np.hsplit(x_train,[x_train.shape[1]-1])
	num_classes = len(np.unique(trainY))
	
	trainY = np.int_(trainY.reshape(-1))
	trainY = np.eye(num_classes)[trainY] #one hot vector
	#print('\n', 'training data loaded successfully!')

	[testX, testY] = np.hsplit(x_test,[x_test.shape[1]-1])
	testY = np.int_(testY.reshape(-1))
	testY = np.eye(num_classes)[testY] #one hot vector
	#print('test data loaded successfully!', '\n')

	return trainX, trainY, testX, testY, num_classes

def nn_performance_metrics(pred_model, pred_true, train_model, train_true):
  precision = precision_score(pred_true, pred_model, average='macro')
  recall = recall_score(pred_true, pred_model, average='macro')
  f1 = f1_score(pred_true, pred_model, average='macro')

  acc_train = accuracy_score(train_true, train_model)
  acc_test = accuracy_score(pred_true, pred_model)

  print("\nTrain accuracy: ", acc_train)
  print("Test accuracy: ", acc_test)

  print("\nTrain error: ", '{0:.2%}'.format(1-acc_train))
  print("Test error: ", '{0:.2%}'.format(1-acc_test))

  return precision, recall, f1, acc_test

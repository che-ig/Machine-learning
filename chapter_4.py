
'''
for iteration in range(25):
    pred = input * weight
    error = (pred - goal_pred) ** 2
    direction_and_amount = (pred - goal_pred) * input
    weight = weight - direction_and_amount

    print("Error:" + str(error) + " Prediction:" + str(pred))
'''
'''
for iteration in range(4):
    pred = input * weight
    error = (pred - goal_pred) ** 2
    delta = pred - goal_pred
    weight_delta = delta * input
    weight = weight - weight_delta
    print("Error:" + str(error) + " Prediction:" + str(pred))
'''

weight, goal_pred, input = (0.5, 0.8, 2)
alpha = 0.1

for iteration in range(20):
    print("-----\nWeight:" + str(weight))
    pred = input * weight
    error = (pred - goal_pred) ** 2
    weight_delta = (pred - goal_pred) * input
    weight = weight - alpha * weight_delta
    print("pred:"+ str(pred) + "  Error:" + str(error) + "  Prediction:" + str(pred))
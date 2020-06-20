import random 

max_generation= 25
capacity = 50
population_size = 8
num_item = 10
val_list = [random.randint(1,15) for x in range(num_item)]
weight_list = [random.randint(1,15) for x in range(num_item)]

def fitness(target):
    weight = 0 
    value = 0
    index = 0
    
    for i in target:
        if index >= num_item:
            break
        if(i == 1):
            value += val_list[index]
            weight += weight_list[index]
        index += 1
    
    if weight > capacity:
        return 0
    else:
        return value

def mutation(target):
    index = random.randint(0,len(target)-1)
    if target[index] == 0:
        target[index] = 1
    else:
        target[index] = 0
        
def crossover(population):
    parent_eligible = 0.3
    parent_lottery = 0.1
    mutation_prob = 0.3
    
    parent_len = int(parent_eligible* len(population))
    parent = population[:parent_len]
    other = population[parent_len:]
    
    for x in other:
        if parent_lottery >random.random():
            parent.append(x)
    
    for y in parent:
        if mutation_prob > random.random():
            mutate(y)
    
    descendant = []
    result_number = len(population) - len(parent)
    
    while len(descendant) < result_number:
        one = random.randint(0,len(parent)-1)
        two = random.randint(0,len(parent)-1)
        first = population[one]
        second = population[two]
        half_len = int(num_item/2)
        mix_child = first[:half_len] + second[half_len:]
        
        if mutation_prob > random.random():
            mutation(mix_child)
        descendant.append(mix_child)
    
    parent.extend(descendant)
    return parent
    
def optimalSolution(target):
    w = 0
    for i in range(len(target)):
        if target[i] == 1:
            w += weight_list[i]
    
    return w == capacity

gen =1
population = [[random.randint(0,0) for x in range(num_item)] for y in range(population_size)]
print("Values :",val_list)
print("Weight :",weight_list)
print("Capacity :",capacity)
print("Population size: ",population_size)
print("Number of item : ",num_item)
for i in range (max_generation):
    print("Generation",gen )
    population = sorted(population,key=lambda x: fitness(x),reverse= True)
    print(population[0] , "Fitness : ", fitness(population[0]))
    if optimalSolution(population[0]) == True:
        break
    
    population = crossover(population)
    gen += 1
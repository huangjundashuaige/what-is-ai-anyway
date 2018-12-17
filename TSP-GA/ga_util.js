// 计算fitness
function calculateFitness() {
    console.log("length" + population.length);
    for (var i = 0; i < population.length; i++) {
        var d = calDistance(cities,population[i]);
        if(d < bestDistance) {
            bestDistance = d;
            best_solution = population[i];
        }
        fitness[i] = 1 / (d + 1);
        
        
    }
    
}

// 转换为概率
function normalized() {
    var sum = 0;
    for(var i = 0; i < fitness.length; i++) {
        sum += fitness[i];
    }
    console.log(sum)

    for(var i = 0; i < fitness.length; i++) {
        fitness[i] = fitness[i] / sum;
        //console.log("fitness[" + i + "]: " + fitness[i]);
    }
}

// 根据概率选择
function pickOne(list, prob) {
    var index = 0;
    var r = random(1);

    while (r > 0) {
        r = r - prob[index];
        index++;

    }

    index--;
    return list[index].slice();
}

// 根据概率进行选择
function getNextGeneration() {
    var newPopulation = [];

    for(var i = 0; i < population.length; i++) {
        // 在这里加上crossover
        var orderA = pickOne(population, fitness);
        var orderB = pickOne(population, fitness);
        var order = crossOver(orderA, orderB);
        //var order = pickOne(population, fitness);
        mutate3(order, 0.05);
        //var new_solution = two_opt_random(order);
        newPopulation[i] = order;
    }

    population = newPopulation;
}

function crossOver(orderA, orderB) {
    var start = floor(random(orderA.length));
    var end = floor(random(start+1, orderA.length));
    var neworder = orderA.slice(start, end);

    for(var i = 0; i < orderB.length; i++) {
        var city = orderB[i];
        if(!neworder.includes(city)) {
            neworder.push(city);
        }
    }
    return neworder;

}

// 随机swap两个下标
function mutate(order, mutationRate) {
    length = order.length;
    for(var i = 0; i < cityNum; i++) {
        if(random(1) < mutationRate) {
            var indexA = floor(random(order.length)); // 我真tm服了你了
            var indexB = floor(random(order.length));
            swap(order, indexA, indexB);
        }
    }
  
}

// 交换邻居下标
function mutate2(order, mutationRate) {
    length = order.length;
    for(var i = 0; i < cityNum; i++) {
        if(random(1) < mutationRate) {
            var indexA = floor(random(order.length));
            var indexB = (indexA + 1) % cityNum;
            swap(order, indexA, indexB);
        }
    }
  
}


// 2-opt
function mutate3(order, mutationRate) {
    length = order.length;
    for(var i = 0; i < cityNum; i++) {
        if(random(1) < mutationRate) {
            order = two_opt_random(order);
            
        }
    }
  
}




function swap(a, i, j) {
    var temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}


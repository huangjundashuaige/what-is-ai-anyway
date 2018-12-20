function calculateTwoCityDistance() {
    for(var i = 0; i < cityNum; i++) {
        for(var j = 0; j < cityNum; j++) {
            dis_arr[i][j] = dist(cities[i].x, cities[i].y, cities[j].x, cities[j].y);
        }
    }

}

function calDistance2(cities, order) {
    var sum = 0;

    for(var i = 0; i < cityNum-1; i++) {
        sum += dis_arr[order[i]][order[i+1]];
    }
    sum += dis_arr[order[cityNum-1]][order[0]];
    return sum;
} 

// 计算fitness
function calculateFitness() {
    currentDistance = Infinity;
    current_solution = order;
    //console.log("length" + population.length);
    for (var i = 0; i < population.length; i++) {
        var d = calDistance2(cities,population[i]);
        //console.log("i:" + i + " " + d);
        if(d < bestDistance) {
            bestDistance = d;
            best_solution = population[i];
        }
        if(d < currentDistance) {
            currentDistance = d;
            current_solution = population[i];
            //console.log("currentDistance:" + currentDistance);
        }
        fitness[i] = 1 / (d + 1);
        
        
    }
    newPopulation.push(current_solution);
    
}

function calculateFitness2() {
    //console.log("length" + newPopulation.length);
    for (var i = 0; i < newPopulation.length; i++) {
        var d = calDistance2(cities,newPopulation[i]);
        
        fitness2[i] = 1 / (d + 1);
        
        
    }
    
}


// 转换为概率
function normalized() {
    var sum = 0;
    for(var i = 0; i < fitness.length; i++) {
        sum += fitness[i];
    }
    //console.log(sum)

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
    //console.log("! " + list[index].slice(0));
    return list[index].slice(0);
}

// 根据概率进行选择

function selection() {
    var parent = [];
    parent.push(current_solution.slice(0));
   // console.log("current solution " + current_solution);
    parent.push(mutate_sym_swap(best_solution.slice(0)).slice(0));
    parent.push(mutate_reorder(best_solution.slice(0)).slice(0));
    parent.push(best_solution.slice(0));

    for(var i = 4; i < populationSize; i++) {
        var tmp = pickOne(population, fitness);
        parent.push(tmp);
    }

    population = parent;
   // console.log("pop len " + population.length );
   // console.log(population);
}

function mutation() {
    for (var i = 0; i < populationSize; i++) {
        if (random(1) < mutate_prob) {
            if (Math.random() > 0.5) {
                population[i] = mutate_reorder(population[i]);
            } else {
                population[i] = mutate_sym_swap(population[i]);
            }
            i--;
        }
    }
}



function midFastCrossOver() {
    var new_selected = [];
    for(var i = 0; i < populationSize; i++) {
        if(random(1) < cross_prob) {
            new_selected.push(i);
        }
    }

    new_selected = shuffle(new_selected);
    
    for(var i = 0; i < new_selected.length-1; i+=2) {
        // var child1 = getChild(1, i, i+1);
        // var child2 = getChild(-1, i, i+1);
        var child1 = crossOver2(population[i], population[i+1]);
        var child2 = crossOver2(population[i], population[i+1]);
        population[i] = child1.slice(0);
        population[i+1] = child2.slice(0);
    }
}

function veryFastCrossOver() {
    var new_selected = [];
    for(var i = 0; i < populationSize; i++) {
        if(random(1) < cross_prob) {
            new_selected.push(i);
        }
    }

    new_selected = shuffle(new_selected);
    
    for(var i = 0; i < new_selected.length-1; i+=2) {
        var child1 = getChild(1, i, i+1);
        var child2 = getChild(-1, i, i+1);
        // var child1 = crossOver2(population[i], population[i+1]);
        // var child2 = crossOver2(population[i], population[i+1]);
        population[i] = child1.slice(0);
        population[i+1] = child2.slice(0);
    }
}


function getChild(fun, x, y) {
    var solution = [];
    var px = [];
    var py = [];
    px = population[x].slice(0);
    py = population[y].slice(0);
    var dx, dy;

    var c = px[floor(random(px.length))];
    solution.push(c);
    while (px.length > 1) {
        // console.log("pxlength " + px.length);
        // console.log("top c " + c);
        var index_x = px.indexOf(c);
        var index_y = py.indexOf(c);
        var index_tmp_x = index_x+fun;
        var index_tmp_y = index_y+fun;
        if(index_tmp_x == -1) {
            index_tmp_x = px.length-1;
        }
        if(index_tmp_y == -1) {
            index_tmp_y = py.length-1;
        }
        if(index_tmp_x == px.length) {
            index_tmp_x = 0;
        }
        if(index_tmp_y == py.length) {
            index_tmp_y = 0;
        }
        // console.log("index_tmp_x " + index_tmp_x);
        // console.log("index_tmp_y " + index_tmp_y);
        dx = px[index_tmp_x];
        dy = py[index_tmp_y];

        var index_x = px.indexOf(c);
        px.splice(index_x, 1);

        var index_y = py.indexOf(c);
        py.splice(index_y, 1);

        var citypoint1 = cities[dx];
        var citypoint2 = cities[dy];
        var citypoint0 = cities[c];
        var d01 = dis_arr[c][dx];
        var d02 = dis_arr[c][dy];
    
        c = d01 < d02 ? dx : dy;
        solution.push(c);
        // console.log("solution");
        // console.log(solution);
    }
  
    return solution;
}


function mutate_sym_swap(order) {
    var start = floor(random(order.length-2));
    var end = floor(random(start+1, order.length-2));
    var times = (end - start + 1) / 2; //交换次数
    for(var i = 0; i < times; i++) {
        swap(order, start+i, end-i);
    }
    return order;
}




// 切下一段基因重新拼接
// 保持一整段不打乱（交换点效果很不好...）
function mutate_reorder(order) {
    var start = floor(random(order.length));
    var end = floor(random(start+1, order.length));
    var segment1 = order.slice(0, start);
    var segment2 = order.slice(start, end);
    var segment3 = order.slice(end, order.length);
    var result = segment2.concat(segment1).concat(segment3);
    return result;
    
}

function newgetNextGeneration() {
    selection();
   // midFastCrossOver();    // generationNum:60000 -> 8405
    veryFastCrossOver();   // generationNum:
    mutation();
    //mutate_old();
    
}

function getNextGeneration() {
    for(var i = 0; i < population.length; i++) {
        // 在这里加上crossover
        var orderA = pickOne(population, fitness);
        var da = calDistance2(cities, orderA);
       // console.log("da " + da);
        var orderB = pickOne(population, fitness);
        var db = calDistance2(cities, orderB);
       // console.log("db " +db);
        var order = crossOver3(orderA, orderB);
        //var order = pickOne(population, fitness);
        mutate(order, 0.05);
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

function crossOver2(orderA, orderB) {
    var random_city_no = floor(random(orderA.length));
    var index_a = orderA.indexOf(random_city_no);
    var index_b = orderB.indexOf(random_city_no);
   // console.log("index_a " + index_a);
   // console.log("index_b " + index_b);
    var index_a_next = (index_a + 1) % cityNum;
    var index_b_next = (index_b + 1) % cityNum;
    var random_city_no_a_next = orderA[index_a_next];
    var random_city_no_b_next = orderB[index_b_next];
    
    // get points
    var A = cities[random_city_no];
    var A_next = cities[random_city_no_a_next];
    var B = cities[random_city_no];
    var B_next = cities[random_city_no_b_next];

    var d1 = dist(A.x, A.y, A_next.x, A_next.y);
    var d2 = dist(B.x, B.y, B_next.x, B_next.y);

    if(d1 > d2) {
        // 交换random_city_no_a_next 与 random_city_no_b_next
        var index1 = orderA.indexOf(random_city_no_a_next);
        var index2 = orderA.indexOf(random_city_no_b_next);
        orderA[index1] = random_city_no_b_next;
        orderA[index2] = random_city_no_a_next;
    }
    

    
    return orderA;

}

function mutate_old() {
    for(var i = 0; i < population.length; i++) {
        mutate(population[i], mutate_prob);
    }
}


function crossOver3(orderA, orderB) {
    var start = floor(random(orderA.length));
    var end = floor(random(start+1, orderA.length));
    var neworder = orderA.slice(start, end);

    // 前面有start个
    // 后面有orderA.length - end 个

    var front_len = start;
    var end_len = orderA.length - end;

    var front = [];
    var end = [];

    var count = 0;

    for(var i = 0; i < orderB.length; i++) {
        var city = orderB[i];
        if(!neworder.includes(city)) {

            if(count < front_len) {
                front.push(city);
            }
            else {
                end.push(city);
            }

            count++;
           // neworder.push(city);
        }
    }

    
    var result = [];
    result = front.concat(neworder);
    result = result.concat(end);

   // console.log("result " + result);
    
    return result;    

}

// 随机swap两个下标
function mutate(order, mutationRate) {
    length = order.length;
    for(var i = 0; i < cityNum; i++) {
        if(random(1) < mutationRate) {
            var indexA = floor(random(order.length));
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

// greedy algorithm to generate initial population
function greedy() {
    //console.log("hey");
    for(var i = 0; i < populationSize; i++) {
        // 以第i个城市为起始点
        var start_city = i;
       
        var solution = [];
        var nonVisited = [...Array(cityNum).keys()];
        // 先将自己remove掉
        var index = nonVisited.indexOf(i);
        nonVisited.splice(index, 1);
        //console.log("nonVisited");
        //console.log(nonVisited);
        
        // 节点i作为第一个城市
        solution.push(i);
        
        var nowCity = cities[i];
        while(nonVisited.length) {
            var minDistance = Infinity;
            var minCityNo = i;
            //console.log("nonv");
            //console.log(nonVisited);
            for(var j = 0; j < nonVisited.length; j++) {
                var d = dist(nowCity.x, nowCity.y, cities[nonVisited[j]].x, cities[nonVisited[j]].y);
                if(d < minDistance) {
                    minDistance = d;
                    minCityNo = nonVisited[j];
                }
            }
            //console.log("minCityNo" + minCityNo);
            // 将minCityNo所指的城市取出
            index = nonVisited.indexOf(minCityNo);
            nonVisited.splice(index, 1);
            // 将minCityNo加入solution
            solution.push(minCityNo);
            //console.log("minCityNo" + minCityNo);
            nowCity = cities[minCityNo];
        }

        //console.log("solution check");
        //console.log(solution);
        population[i] = solution;
    }

}
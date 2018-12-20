var cities = [];
var cityNum = 150
var order = [...Array(cityNum).keys()];
var generationNum = 60000;
var fitness = [];
var fitness2 = [];
var populationSize = 30;
var bestDistance = Infinity;
var best_solution = order;
var current_solution = order;
var currentDistance = Infinity;
var population = [];
var newPopulation = [];
var generationIndex = 1;
var cross_prob = 0.9;
var mutate_prob = 0.01;


var alpha = 0.8;

var dis_arr = new Array();
for(var i = 0; i < cityNum; i++) {
    dis_arr[i] = new Array();
    for(var j = 0; j < cityNum; j++) {
        dis_arr[i][j] = Infinity;
    }
}



function initialData() {
    var test = random(1);
    print("test "+test);
    cities[0] = createVector(37.4393516691, 541.2090699418);
    cities[1] = createVector(612.1759508571, 494.3166877396);
    cities[2] = createVector(38.1312338227, 353.1484581781);
    cities[3] = createVector(53.4418081065, 131.484901365);
    cities[4] = createVector(143.0606355347, 631.7200953923);
    cities[5] = createVector(689.9451267256, 468.5354998742);
    cities[6] = createVector(112.7478815786, 529.417757826);
    cities[7] = createVector(141.4875865042, 504.818485571);
    cities[8] = createVector(661.0513901702, 445.9375182115);
    cities[9] = createVector(98.7899036592, 384.5926031158);
    cities[10] = createVector(697.3881696597, 180.3962284275);
    cities[11] = createVector(536.4894189738, 287.2279085051);
    cities[12] = createVector(192.4067320507, 20.439405931);
    cities[13] = createVector(282.7865258765, 229.8001556189);
    cities[14] = createVector(240.8251726391, 281.51414372);
    cities[15] = createVector(246.9281323057, 322.461332116);
    cities[16] = createVector(649.7313216456, 62.3331575282);
    cities[17] = createVector(352.96585626, 666.7873101942);
    cities[18] = createVector(633.392367658, 534.9398453712);
    cities[19] = createVector(488.311799404, 437.4869439948);
    cities[20] = createVector(141.4039286509, 228.4325551488);
    cities[21] = createVector(17.3632612602, 240.2407068508);
    cities[22] = createVector(397.5586451389, 231.3591208928);
    cities[23] = createVector(565.7853781464, 282.3858748974);
    cities[24] = createVector(475.8975387047, 468.5392706317);
    cities[25] = createVector(322.4224566559, 550.3165478233);
    cities[26] = createVector(397.5586634023, 74.7588387765);
    cities[27] = createVector(672.8618339396, 432.882640963);
    cities[28] = createVector(571.2189680147, 530.261699153);
    cities[29] = createVector(104.6531165914, 482.8224768783);
    cities[30] = createVector(356.7098388794, 67.6477131712);
    cities[31] = createVector(400.4070255527, 253.6794479997);
    cities[32] = createVector(282.3036243109, 426.8380500923);
    cities[33] = createVector(58.7766988363, 507.1712386832);
    cities[34] = createVector(189.75062244, 460.3815233617);
    cities[35] = createVector(659.9124120147, 226.6284156239);
    cities[36] = createVector(639.0307636033, 467.2302300719);
    cities[37] = createVector(415.0258357432, 233.3045376118);
    cities[38] = createVector(547.2662016307, 161.6589278401);
    cities[39] = createVector(616.6547902644, 339.3409309407);
    cities[40] = createVector(494.8592427417, 148.1217856389);
    cities[41] = createVector(629.9980812186, 433.4548164038);
    cities[42] = createVector(471.101431241, 314.2219307579);
    cities[43] = createVector(138.2440514421, 137.1679919735);
    cities[44] = createVector(91.5847556724, 110.0203007516);
    cities[45] = createVector(390.6972811808, 423.9774318385);
    cities[46] = createVector(565.1617825137, 429.1598152874);
    cities[47] = createVector(54.5248980387, 438.5515408431);
    cities[48] = createVector(334.350832971, 153.796923804);
    cities[49] = createVector(531.0291024509, 612.3874827889);
    cities[50] = createVector(475.7345905802, 385.7844618897);
    cities[51] = createVector(228.8325218994, 410.4461939615);
    cities[52] = createVector(578.3805347586, 321.3303494537);
    cities[53] = createVector(358.9170574485, 404.4670352898);
    cities[54] = createVector(486.4648554867, 593.0429937016);
    cities[55] = createVector(343.169370767, 509.3123571315);
    cities[56] = createVector(530.3626972076, 137.6881275684);
    cities[57] = createVector(498.8065475299, 576.2102674608);
    cities[58] = createVector(224.31827155, 312.4677490415);
    cities[59] = createVector(595.836073259, 81.8130051356);
    cities[60] = createVector(661.5588724308, 217.0456944477);
    cities[61] = createVector(43.6892045516, 305.4722789165);
    cities[62] = createVector(79.465345253, 445.9641737689);
    cities[63] = createVector(210.4163247004, 130.7151137038);
    cities[64] = createVector(432.2642292251, 629.4092661116);
    cities[65] = createVector(623.2487161301, 69.189285084);
    cities[66] = createVector(436.5194739944, 282.935645607);
    cities[67] = createVector(59.4163265482, 40.1280234442);
    cities[68] = createVector(630.9230074073, 230.342988813);
    cities[69] = createVector(579.3265539688, 601.0359410602);
    cities[70] = createVector(117.862450748, 112.9796833705);
    cities[71] = createVector(297.7912565664, 166.3131886803);
    cities[72] = createVector(22.7642703744, 455.5340094037);
    cities[73] = createVector(259.7095810385, 10.6199925885);
    cities[74] = createVector(342.3579873647, 599.3880182608);
    cities[75] = createVector(10.0260950143, 488.9310558282);
    cities[76] = createVector(315.2926064118, 273.2275475579);
    cities[77] = createVector(220.7044919297, 270.0819745721);
    cities[78] = createVector(192.1186059948, 314.1839922798);
    cities[79] = createVector(271.5042718992, 225.2921989972);
    cities[80] = createVector(530.7320005441, 504.0670155337);
    cities[81] = createVector(42.5331441666, 656.3645162886);
    cities[82] = createVector(396.1274792588, 539.4648066027);
    cities[83] = createVector(118.6631474021, 508.7129103929);
    cities[84] = createVector(395.6913876595, 699.5376048429);
    cities[85] = createVector(559.0157105844, 560.8866941411);
    cities[86] = createVector(22.6471035906, 526.2470392816);
    cities[87] = createVector(135.6377085256, 325.8409901555);
    cities[88] = createVector(141.4507014379, 485.2477927763);
    cities[89] = createVector(396.7741299332, 460.7557115283);
    cities[90] = createVector(87.7494562765, 19.6170129082);
    cities[91] = createVector(350.4245639661, 420.6531186835);
    cities[92] = createVector(216.7010817133, 466.4816410995);
    cities[93] = createVector(130.9237737024, 351.1491733079);
    cities[94] = createVector(72.6329856671, 645.7852219213);
    cities[95] = createVector(144.6002949996, 457.4224283926);
    cities[96] = createVector(212.3725077442, 594.9216893413);
    cities[97] = createVector(49.9186786455, 541.4350825349);
    cities[98] = createVector(656.6943525585, 558.1109593509);
    cities[99] = createVector(176.5941623792, 648.5239953299);
    cities[100] = createVector(500.3825200226, 198.7428378322);
    cities[101] = createVector(634.317867842, 612.8291643194);
    cities[102] = createVector(59.7537372726, 551.6321886765);
    cities[103] = createVector(15.2145765106, 143.0441928532);
    cities[104] = createVector(283.0054378872, 376.4439530184);
    cities[105] = createVector(146.5389000907, 39.4231794338);
    cities[106] = createVector(101.8685605377, 635.098685018);
    cities[107] = createVector(588.1968537448, 580.5946976921);
    cities[108] = createVector(457.2628632528, 350.0164047376);
    cities[109] = createVector(537.4663680494, 472.5842276692);
    cities[110] = createVector(269.3669098585, 367.4763636538);
    cities[111] = createVector(239.9045383695, 102.629765339);
    cities[112] = createVector(88.4677500396, 384.0507209275);
    cities[113] = createVector(658.9133693395, 583.9575181023);
    cities[114] = createVector(97.7359146347, 157.4558657632);
    cities[115] = createVector(506.6191384007, 233.0022156094);
    cities[116] = createVector(500.2566898239, 64.9136393489);
    cities[117] = createVector(594.4048565021, 275.874186899);
    cities[118] = createVector(66.230814661, 24.1317387604);
    cities[119] = createVector(598.4162993909, 414.5557574275);
    cities[120] = createVector(172.308833083, 344.3963466366);
    cities[121] = createVector(299.48128518, 251.829512132);
    cities[122] = createVector(303.8379894831, 21.052606379);
    cities[123] = createVector(197.896926984, 512.388896098);
    cities[124] = createVector(56.0199567669, 243.0663818382);
    cities[125] = createVector(255.5566183121, 448.8651882442);
    cities[126] = createVector(608.4256112402, 222.5421309272);
    cities[127] = createVector(70.2722703273, 77.9227026433);
    cities[128] = createVector(398.2298999899, 119.557657386);
    cities[129] = createVector(635.4970237093, 133.3225902609);
    cities[130] = createVector(378.3484559418, 272.2907677147);
    cities[131] = createVector(484.8029663388, 677.0730379436);
    cities[132] = createVector(278.8710882619, 299.9308770828);
    cities[133] = createVector(381.6537300653, 360.3337602785);
    cities[134] = createVector(557.6070707573, 595.3185092281);
    cities[135] = createVector(249.0589749342, 76.6595112599);
    cities[136] = createVector(562.9048787838, 670.0382113114);
    cities[137] = createVector(398.550436558, 392.6493259144);
    cities[138] = createVector(590.893972056, 370.7414913742);
    cities[139] = createVector(558.2008003726, 0.4198814512);
    cities[140] = createVector(461.4114714423, 530.5254969413);
    cities[141] = createVector(354.7242881504, 685.40453619);
    cities[142] = createVector(193.6611295657, 669.7432521028);
    cities[143] = createVector(352.3140807211, 140.3273323662);
    cities[144] = createVector(308.434570974, 115.2054269847);
    cities[145] = createVector(299.588137008, 530.588961902);
    cities[146] = createVector(334.2748764383, 152.1494569394);
    cities[147] = createVector(690.9658585947, 134.5793307203);
    cities[148] = createVector(48.0798124069, 270.968067372);
    cities[149] = createVector(91.6467647724, 166.3541158474);
}

function setup() {
    // 初始化数据
    initialData();

    createCanvas(725, 800);
    //////////////test
    var bst = [ 0, 97, 102, 81, 94, 106, 4, 99, 142, 96, 145, 25, 74, 17, 141, 84, 64, 131, 136, 49, 54, 57, 140, 82, 55, 89, 45, 91, 53, 137, 133, 130, 31, 22, 37, 66, 42, 108, 50, 19, 24, 109, 80, 28, 85, 134, 69, 107, 101, 113, 98, 18, 1, 36, 5, 27, 8, 41, 119, 46, 138, 39, 52, 117, 23, 11, 115, 100, 40, 56, 38, 126, 68, 35, 60, 10, 147, 129, 16, 65, 59, 139, 116, 128, 26, 30, 122, 73, 12, 105, 90, 118, 67, 127, 44, 70, 43, 63, 111, 135, 144, 143, 48, 146, 71, 79, 13, 121, 76, 132, 14, 77, 20, 149, 114, 3, 103, 21, 124, 148, 61, 2, 112, 9, 93, 87, 120, 78, 58, 15, 110, 104, 32, 125, 51, 92, 123, 34, 95, 88, 7, 6, 83, 29, 62, 47, 72, 75, 33, 86]; 
        
    var bst_distance = calDistance2(cities, bst);
    console.log("bst: " + bst_distance);
            
    // 先做一个局部搜索
    two_opt();

    // 随机产生一个种群
    for(var i = 0; i < populationSize; i++) {
        population[i] = shuffle(order);
        console.log(i);
    }

    calculateTwoCityDistance();

    //greedy to generate some solutions
    //greedy();
    

   
}

function draw() {

    
    
    
    console.log("best_solution:");
    console.log(best_solution);
    console.log("best distance:");
    console.log(bestDistance);
 
    background(0);
    
    fill(255);
    for (var i = 0; i < best_solution.length; i++) {
        ellipse(cities[best_solution[i]].x, cities[best_solution[i]].y, 10, 10);
       
    }

    stroke(255);
    strokeWeight(2);
    noFill();
    beginShape();
    for (var i = 0; i < best_solution.length; i++) {
        vertex(cities[best_solution[i]].x, cities[best_solution[i]].y);
    }
    vertex(cities[best_solution[0]].x, cities[best_solution[0]].y);
    endShape();

    beginShape();
    textSize(64);
    var s = '';
    s += "best distance: " + bestDistance;
    
    fill(255);
    text(s, 8, 780);
    endShape();

    console.log("generationIndex:" + generationIndex);

    // 停止循环画图
    if(generationIndex > generationNum) { noLoop(); }

    // GA 部分
    // 计算群落中的最优值 进行更新
    if(generationIndex <= generationNum) {

        calculateFitness();      // 计算每个个体的适应值  1/(d+1)  距离越短适应值越高
        normalized();     // 将适应值转变为概率
        newgetNextGeneration();        // 产生下一代
        generationIndex++;
    
    }

}

function swap(a, i, j) {
    var temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

function two_opt() {
    for (var i = 0; i < cityNum-1; i++) {
        for (var j = i+1; j < cityNum; j++) {
            //if (i == j) { continue; }
            
           // var tmp = cities.slice();
            var left = order.slice(0, i);
            var mid = order.slice(i, j+1);
            var right = order.slice(j+1);
            mid.reverse();
            tmp = left.concat(mid);
            tmp = tmp.concat(right);
        
            var now_distance = calDistance2(cities, tmp);
            if(now_distance < bestDistance) {
                bestDistance = now_distance;
                best_solution = tmp;
            }
            
        }
    }
}

function init_solution(order) {
    var init_order = shuffle(order);
    return init_order;
}
function two_opt_random(order) {
    // now 0 - 10
    var left_index = 0;
    var right_index = 0;
    while(left_index == right_index) {
        left_index = floor(random(0, cityNum));
        right_index = floor(random(left_index+1, cityNum));
    }

    var left = order.slice(0, left_index);
    var mid = order.slice(left_index, right_index+1);
    var right = order.slice(right_index+1);
    mid.reverse();
    tmp = left.concat(mid);
    tmp = tmp.concat(right);

    // return a new order
    return tmp;
}



function calDistance(points, order) {
    var sum = 0;
    
    for (var i = 0; i < points.length-1; i++) {
        
        var d = dist(points[order[i]].x, points[order[i]].y, points[order[i+1]].x, points[order[i+1]].y);
        sum += d;
    }

    sum += dist(points[order[points.length-1]].x, points[order[points.length-1]].y, points[order[0]].x, points[order[0]].y);
   

    return sum;
}


from type_checking import *
class MaxScore:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        sumdic=dict()
        def submax(i,j,curIdx):
            if (i,j,curIdx) not in sumdic:
                # print(sumdic)
                if curIdx==len(multipliers)-1:
                    res = max(nums[i] * multipliers[curIdx], nums[j-1] * multipliers[curIdx])
                else:
                    popleft = submax(i+1,j,curIdx+1) + nums[i] * multipliers[curIdx]
                    popright = submax(i,j-1,curIdx+1) + nums[j-1] * multipliers[curIdx]

                    res = max(popleft,popright)

                sumdic[(i,j,curIdx)] = res

            return sumdic[(i,j,curIdx)]

        return submax(0,len(nums),0)
s = MaxScore()
a=[-85,-863,-579,101,922,-132,-4,764,-503,822,-65,58,-442,247,355,433,-164,993,-697,359,304,-411,847,-336,18,-885,-162,-702,-8,118,-798,900,790,781,-824,-292,138,252,124,306,-654,-592,-760,449,-390,-413,642,546,-779,-459,801,-440,-973,-321,-208,546,219,211,-200,211,51,-702,-164,-615,486,-993,418,512,902,-437,-867,-245,587,-843,188,833,-248,-492,583,-941,770,863,-997,247,772,-917,-439,-455,-837,-256,466,564,-100,-435,-438,-728,793,-828,662,53,858,-353,-964,273,-719,394,-746,-615,768,401,198,-166,564,858,-566,-993,-573,431,-417,-422,368,-976,-474,-336,-603,189,6,-913,894,516,833,144,716,-243,771,476,-908,845,994,-474,412,578,29,-344,-720,299,512,145,537,-787,815,806,311,-243,-898,750,-121,844,-453,-13,211,371,-908,-359,-680,-210,48,470,-598,-922,-92,-389,-634,965,-229,-855,105,745,-745,1,582,-728,-242,-648,337,402,169,-531,588,-571,702,-653,-145,9,-326,851,-552,-301,140,934,346,811,-602,405,623,-633,903,269,274,-353,137,-905,911,822,56,-906,-624,-856,-47,806,315,-291,-414,-710,708,273,219,382,710,-149,143,-907,-23,944,-628,801,898,264,613,411,-288,680,-726,133,-542,572,95,-719,292,-90,788,-635,328,-921,-941,-733,628,91,372,-192,980,-894,467,574,508,-70,-993,203,879,430,-444,954,58,-704,-787,998,-298,968,-382,469,718,-680,-35,-516,802,931,764,-435,-22,-44,-247,67,-786,822,366,867,-422,245,906,215,-496,237,-427,289,399,186,296,-382,-450,-765,-891,668,-15,316,-234,-854,242,788,-853,-890,-740,-48,147,-856,-801,-696,-72,59,-593,317,100,-905,-728,747,-89,-22,-580,121,361,-366,521,729,-963,-702,-96,774,-390,634,406,532,-775,939,-420,103,-577,236,736,-103,506,-197,918,-94,-623,876,247,-865,284,-419,-636,668,-259,523,-992,24,-302,881,739,-643,811,741,-340,816,645,-365,381,-779,18,282,34,-648,-791,-944,-926,-516,687,931,-869,-533,120,-995,-934,526,198,454,-38,-181,-27,727,236,-72,-308,-153,873,-361,128,690,-515,476,-793,-542,58,-325,212,255,20,-711,223,-790,496,-783,524,413,123,186,0,83,586,185,-593,261,-492,-761,-692,170,89,234,-1,973,-36,236,-450,-865,-333,-871,330,958,-646,-269,-112,-2,-257,593,-77,809,-353,-113,-388,-866,-935,492,247,-409,-82,-192,154,908,906,-227,-182,260,790,223,-983,-888,661,-75,-236,791,-587,481,-376,136,213,957,-306,-967,531,401,160,213,-856,841,932,-709,281,-843,905,-543,990,-391,685,-79,509,978,224,132,-998,860,-754,964,773,-861,382,109,364,-184,645,-449,-969,203,-487,670,667,525,-751,-202,547,-61,951,-713,-623,241,539,-127,-528,412,236,-61,532,-867,-344,-399,590,221,-991,720,888,430,-61,-340,737,-435,998,-8,-22,-315,-206,-594,233,395,341,252,-854,-352,761,-932,-966,229,996,592,-120,221,736,-931,162,-260,275,-172,336,-998,-975,-219,-253,699,-201,-216,-505,845,862,100,519,339,268,776,537,-1000,-390,-7,-604,640,-382,327,316,-20,83,537,-766,-633,-459,-922,528,-992,37,-433,-920,-925,-609,780,-818,-639,836,671,722,-615,269,-21,167,804,-690,654,-958,-581,-706,-290,47,-966,-357,-893,-177,592,173,873,-234,303,-765,775,930,824,416,-495,414,944,-908,-973,-26,748,240,455,-945,766,194,-302,-706,443,-645,315,177,-151,353,992,596,-941,317,-172,-191,-836,-436,862,-439,679,581,690,-832,-107,395,-525,-554,-28,-601,377,589,-526,-693,-837,292,722,797,994,956,626,-205,-270,12,911,736,448,-755,529,-933,-973,692,-705,311,-467,-723,-411,315,-802,-681,735,-392,183,94,371,318,331,181,462,-465,-14,-813,482,170,428,529,877,-427,-677,-165,-97,-325,-630,-366,567,455,245,-77,733,-551,290,441,-409,914,-810,-420,-853,-413,-646,840,638,270,953,-153,-297,112,-942,-924,-248,-578,117,-785,-262,920,-274,36,942,-771,869,479,252,-14,15,39,-654,-875,44,-182,572,935,314,-621,141,-748,456,-234,119,525,-701,-842,277,-325,-523,120,268,-163,-639,-137]
b= [663,218,-204,527,380,-838,-31,542,-775,333,-368,921,295,-407,682,-662,-872,-21,430,933,-860,169,-892,615,25,-205,-664,-233,829,171,714,316,-857,334,397,-557,-748,-604,-123,790,-926,-465,537,-87,993,483,-449,-600,-602,-306,974,719,-329,-739,-524,647,182,-571,422,-322,405,-716,831,553,-697,608,349,-211,20,-475,-121,-114,92,-519,-658,144,-745,472,-124,-988,93,-461,-916,588,191,463,-82,-507,-249,-25,-689,404,962,142,813,-934,375,-504,-197,973,-892,-109,-314,703,-582,-198,154,672,380,-883,937,-410,-828,60,48,-54,-342,-477,-178,283,364,114,-813,-16,191,632,-101,-984,-416,80,-563,457,-136,-50,647,723,-699,128,856,-166,-923,149,85,749,-812,964,-329,-995,-199,-307,-80,366,-546,768,-927,553,-338,-515,-519,-22,-304,888,171,-862,611,-51,911,444,511,-946,719,161,-26,585,48,118,-770,557,-581,47,-925,209,174,-211,-489,-687,-432,200,499,-45,-638,967,-745,440,271,-694,145,-623,702,-537,731,-702,-979,-766,277,627,-637,-507,565,533,870,866,456,851,-217,634,-281,92,-954,-50,104,895,133,803,-308,-857,469,-766,-153,555,823,-974,594,398,-956,997,-191,-654,415,-145,-632,770,-20,149,-900,-231,639,417,847,732,-760,367,522,56,-643,266,899,566,-601,-768,-728,-390,809,-26,-132,-710,-580,610,-754,-761,268,-526,-876,-747,512,512,-520,-404,-333,-967,949,-712,807,215,554,-476,520,-226,779,404,210,-399,339,-981,602,-858,478,-791,982,-31,363,-453,-578,-96,-397,16,317,302,-132,755,483,606,25,46,-116,-792,-748,346,935,683,231,-578,-682,866,302,-13,535,-899,-324,-92,124,-693,324,482,642,769,942,911,-500,761,-557,-923,-593,-595,-6,222,757,-65,8,-248,562,-602,852,27,-105,567,488,-355,650,144,643,-11,487,-90,311,-233,96,-309,984,279,-865,-5,-809,829,591,-839,-576,-861,-739,665,911,274,-973,-893,446,-662,405,737,-745,298,-145,957,-210,-757,614,368,228,-522,-377,-718,347,465,-272,-472,-288,436,198,-311,-833,-67,44,887,-454,-539,-329,560,-367,-700,-109,661,405,67,-492,491,296,-582,207,-129,759,662,-111,-124,607,75,-889,-25,489,958,-858,-8,-720,445,-157,-605,5,-290,511,-896,-358,-907,-448,-840,391,88,-441,-494,358,309,-40,-996,724,-849,-663,-190,352,131,637,782,430,503,965,320,-30,171,202,-379,-212,966,-391,133,913,-146,640,484,798,-803,-703,-454,-669,656,446,249,950,-145,536,738,908,4,488,727,614,787,558,-226,-710,-461,148,110,279,596,-36,-580,-169,-385,-592,-692,-493,665,-37,-903,812,-39,-113,48,640,-124,664,-119,-547,-823,490,-955,482,-840,695,336,-619,-707,-975,-360,944,843,898,-557,853,-282,-954,-44,-614,415,-67,920,675,-276,-515,-978,82,-770,695,-226,884,621,719,-279,-102,656,-946,-744,-210,-100,981,657,672,313,914,293,-891,-838,-644,607,-195,425,940,490,176,-900,23,-913,9,-574,732,559,904,-676,652,613,-590,748,772,-80,-278,194,217,632,-537,803,709,304,665,-792,-767,-473,681,715,867,785,-579,-473,692,-137,966,-752,751,849,176,698,579,861,452,-266,782,-838,-177,37,210,-157,126,244,805,786,897,-357,364,-579,254,-877]


a=[-85,-863,-579,101,922,-132,-4,764,-503,822,-65,58,-442,247,355,433,-164,993,-697,359,304,-411,847,-336,18,-885,-162,-702,-8,118,-798,900,790,781,-824,-292,138,252,124,306,-654,-592,-760,449,-390,-413,642,546,-779,-459,801,-440,-973,-321,-208,546,219,211,-200,211,51,-702,-164,-615,486,-993,418,512,902,-437,-867,-245,587,-843,188,833,-248,-492,583,-941,770,863,-997,247,772,-917,-439,-455,-837,-256,466,564,-100,-435,-438,-728,793,-828,662,53,858,-353,-964,273,-719,394,-746,-615,768,401,198,-166,564,858,-566,-993,-573,431,-417,-422,368,-976,-474,-336,-603,189,6,-913,894,516,833,144,716,-243,771,476,-908,845,994,-474,412,578,29,-344,-720,299,512,145,537,-787,815,806,311,-243,-898,750,-121,844,-453,-13,211,371,-908,-359,-680,-210,48,470,-598,-922,-92,-389,-634,965,-229,-855,105,745,-745,1,582,-728,-242,-648,337,402,169,-531,588,-571,702,-653,-145,9,-326,851,-552,-301,140,934,346,811,-602,405,623,-633,903,269,274,-353,137,-905,911,822,56,-906,-624,-856,-47,806,315,-291,-414,-710,708,273,219,382,710,-149,143,-907,-23,944,-628,801,898,264,613,411,-288,680,-726,133,-542,572,95,-719,292,-90,788,-635,328,-921,-941,-733,628,91,372,-192,980,-894,467,574,508,-70,-993,203,879,430,-444,954,58,-704,-787,998,-298,968,-382,469,718,-680,-35,-516,802,931,764,-435,-22,-44,-247,67,-786,822,366,867,-422,245,906,215,-496,237,-427,289,399,186,296,-382,-450,-765,-891,668,-15,316,-234,-854,242,788,-853,-890,-740,-48,147,-856,-801,-696,-72,59,-593,317,100,-905,-728,747,-89,-22,-580,121,361,-366,521,729,-963,-702,-96,774,-390,634,406,532,-775,939,-420,103,-577,236,736,-103,506,-197,918,-94,-623,876,247,-865,284,-419,-636,668,-259,523,-992,24,-302,881,739,-643,811,741,-340,816,645,-365,381,-779,18,282,34,-648,-791,-944,-926,-516,687,931,-869,-533,120,-995,-934,526,198,454,-38,-181,-27,727,236,-72,-308,-153,873,-361,128,690,-515,476,-793,-542,58,-325,212,255,20,-711,223,-790,496,-783,524,413,123,186,0,83,586,185,-593,261,-492,-761,-692,170,89,234,-1,973,-36,236,-450,-865,-333,-871,330,958,-646,-269,-112,-2,-257,593,-77,809,-353,-113,-388,-866,-935,492,247,-409,-82,-192,154,908,906,-227,-182,260,790,223,-983,-888,661,-75,-236,791,-587,481,-376,136,213,957,-306,-967,531,401,160,213,-856,841,932,-709,281,-843,905,-543,990,-391,685,-79,509,978,224,132,-998,860,-754,964,773,-861,382,109,364,-184,645,-449,-969,203,-487,670,667,525,-751,-202,547,-61,951,-713,-623,241,539,-127,-528,412,236,-61,532,-867,-344,-399,590,221,-991,720,888,430,-61,-340,737,-435,998,-8,-22,-315,-206,-594,233,395,341,252,-854,-352,761,-932,-966,229,996,592,-120,221,736,-931,162,-260,275,-172,336,-998,-975,-219,-253,699,-201,-216,-505,845,862,100,519,339,268,776,537,-1000,-390,-7,-604,640,-382,327,316,-20,83,537,-766,-633,-459,-922,528,-992,37,-433,-920,-925,-609,780,-818,-639,836,671,722,-615,269,-21,167,804,-690,654,-958,-581,-706,-290,47,-966,-357,-893,-177,592,173,873,-234,303,-765,775,930,824,416,-495,414,944,-908,-973,-26,748,240,455,-945,766,194,-302,-706,443,-645,315,177,-151,353,992,596,-941,317,-172,-191,-836,-436,862,-439,679,581,690,-832,-107,395,-525,-554,-28,-601,377,589,-526,-693,-837,292,722,797,994,956,626,-205,-270,12,911,736,448,-755,529,-933,-973,692,-705,311,-467,-723,-411,315,-802,-681,735,-392,183,94,371,318,331,181,462,-465,-14,-813,482,170,428,529,877,-427,-677,-165,-97,-325,-630,-366,567,455,245,-77,733,-551,290,441,-409,914,-810,-420,-853,-413,-646,840,638,270,953,-153,-297,112,-942,-924,-248,-578,117,-785,-262,920,-274,36,942,-771,869,479,252,-14,15,39,-654,-875,44,-182,572,935,314,-621,141,-748,456,-234,119,525,-701,-842,277,-325,-523,120,268,-163,-639,-137]
b= [663,218,-204,527,380,-838,-31,542,-775,333,-368,921,295,-407,682,-662,-872,-21,430,933,-860,169,-892,615,25,-205,-664,-233,829,171,714,316,-857,334,397,-557,-748,-604,-123,790,-926,-465,537,-87,993,483,-449,-600,-602,-306,974,719,-329,-739,-524,647,182,-571,422,-322,405,-716,831,553,-697,608,349,-211,20,-475,-121,-114,92,-519,-658,144,-745,472,-124,-988,93,-461,-916,588,191,463,-82,-507,-249,-25,-689,404,962,142,813,-934,375,-504,-197,973,-892,-109,-314,703,-582,-198,154,672,380,-883,937,-410,-828,60,48,-54,-342,-477,-178,283,364,114,-813,-16,191,632,-101,-984,-416,80,-563,457,-136,-50,647,723,-699,128,856,-166,-923,149,85,749,-812,964,-329,-995,-199,-307,-80,366,-546,768,-927,553,-338,-515,-519,-22,-304,888,171,-862,611,-51,911,444,511,-946,719,161,-26,585,48,118,-770,557,-581,47,-925,209,174,-211,-489,-687,-432,200,499,-45,-638,967,-745,440,271,-694,145,-623,702,-537,731,-702,-979,-766,277,627,-637,-507,565,533,870,866,456,851,-217,634,-281,92,-954,-50,104,895,133,803,-308,-857,469,-766,-153,555,823,-974,594,398,-956,997,-191,-654,415,-145,-632,770,-20,149,-900,-231,639,417,847,732,-760,367,522,56,-643,266,899,566,-601,-768,-728,-390,809,-26,-132,-710,-580,610,-754,-761,268,-526,-876,-747,512,512,-520,-404,-333,-967,949,-712,807,215,554,-476,520,-226,779,404,210,-399,339,-981,602,-858,478,-791,982,-31,363,-453,-578,-96,-397,16,317,302,-132,755,483,606,25,46,-116,-792,-748,346,935,683,231,-578,-682,866,302,-13,535,-899,-324,-92,124,-693,324,482,642,769,942,911,-500,761,-557,-923,-593,-595,-6,222,757,-65,8,-248,562,-602,852,27,-105,567,488,-355,650,144,643,-11,487,-90,311,-233,96,-309,984,279,-865,-5,-809,829,591,-839,-576,-861,-739,665,911,274,-973,-893,446,-662,405,737,-745,298,-145,957,-210,-757,614,368,228,-522,-377,-718,347,465,-272,-472,-288,436,198,-311,-833,-67,44,887,-454,-539,-329,560,-367,-700,-109,661,405,67,-492,491,296,-582,207,-129,759,662,-111,-124,607,75,-889,-25,489,958,-858,-8,-720,445,-157,-605,5,-290,511,-896,-358,-907,-448,-840,391,88,-441,-494,358,309,-40,-996,724,-849,-663,-190,352,131,637,782,430,503,965,320,-30,171,202,-379,-212,966,-391,133,913,-146,640,484,798,-803,-703,-454,-669,656,446,249,950,-145,536,738,908,4,488,727,614,787,558,-226,-710,-461,148,110,279,596,-36,-580,-169,-385,-592,-692,-493,665,-37,-903,812,-39,-113,48,640,-124,664,-119,-547,-823,490,-955,482,-840,695,336,-619,-707,-975,-360,944,843,898,-557,853,-282,-954,-44,-614,415,-67,920,675,-276,-515,-978,82,-770,695,-226,884,621,719,-279,-102,656,-946,-744,-210,-100,981,657,672,313,914,293,-891,-838,-644,607,-195,425,940,490,176,-900,23,-913,9,-574,732,559,904,-676,652,613,-590,748,772,-80,-278,194,217,632,-537,803,709,304,665,-792,-767,-473,681,715,867,785,-579,-473,692,-137,966,-752,751,849,176,698,579,861,452,-266,782,-838,-177,37,210,-157,126,244,805,786,897,-357,364,-579,254,-877]
s.maximumScore(a,b)

c=[1,2,3]
d=[3,2,1]
s.maximumScore(a,b)
s.maximumScore(c,d)

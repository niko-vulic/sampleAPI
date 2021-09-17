# 45. Jump Game II
#
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

from typing import List


class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "jump"

    def defineTestCases(self):
        # self.testCases.append([0, 1, 2])
        self.testCases.append([2, 3, 1, 1, 4])
        self.testCases.append([1, 2, 3])
        self.testCases.append([2, 1])
        self.testCases.append([1,1,1,1])
        # self.testCases.append([509,998,692,189,318,238,939,590,267,457,662,404,546,192,385,704,342,220,746,821,162,899,809,833,88,596,83,239,497,396,843,447,992,466,120,467,923,89,400,544,219,18,832,310,911,696,565,403,241,28,683,779,723,474,119,558,598,656,831,21,23,333,247,44,651,823,43,375,71,613,385,37,307,581,754,318,219,936,560,354,1,368,814,419,77,620,193,823,519,91,787,939,825,920,820,174,472,656,194,866,420,910,112,292,946,447,117,505,359,498,679,938,958,651,80,331,78,162,810,350,745,374,637,949,425,578,710,45,549,210,443,853,908,710,603,843,330,868,820,836,237,860,55,879,925,244,49,324,914,992,910,219,499,647,57,143,991,809,177,399,103,854,791,403,382,302,235,757,203,278,242,174,65,507,818,319,901,973,255,213,81,836,860,455,567,487,705,684,79,553,44,739,473,628,305,987,996,852,363,890,87,366,553,24,57,184,422,456,241,823,202,245,928,661,42,83,852,278,142,600,302,482,795,308,424,569,61,630,785,51,750,115,364,468,251,51,934,186,688,938,496,805,404,695,21,13,943,505,121,907,39,833,201,489,302,593,870,110,925,844,241,814,991,914,366,780,125,822,984,581,742,174,588,210,288,444,68,338,708,670,320,944,356,258,509,72,626,659,675,839,394,915,282,124,663,691,219,284,304,732,103,196,893,252,723,706,810,89,505,739,31,184,27,690,671,35,180,112,353,106,506,402,290,667,513,430,921,715,400,320,21,641,367,991,311,615,587,508,396,163,861,72,336,187,515,415,486,896,253,480,563,444,329,545,372,286,956,707,553,91,447,163,956,611,588,899,715,108,512,727,918,344,792,388,805,54,588,614,157,109,95,966,988,362,723,248,43,952,285,603,949,286,546,842,426,855,193,39,28,671,21,280,451,450,440,884,300,663,359,452,56,484,729,322,214,674,3,18,837,205,421,311,734,825,948,854,234,401,724,903,427,757,597,120,425,43,778,603,379,698,663,57,169,647,100,965,290,705,720,879,972,209,601,12,298,825,157,820,150,221,698,851,83,408,740,310,74,429,674,888,661,415,872,686,193,216,745,933,826,709,211,336,720,830,418,485,592,246,362,394,447,406,9,497,697,232,617,990,969,416,695,143,485,732,432,490,107,530,443,882,390,632,127,34,48,98,836,13,896,295,702,179,873,299,607,595,214,843,622,940,359,870,980,455,431,174,18,618,177,312,941,862,735,850,495,659,480,705,995,83,922,238,219,765,526,668,375,995,777,295,611,526,992,908,600,531,45,531,607,729,624,151,962,506,45,961,23,314,222,12,841,546,139,197,355,823,595,731,334,779,355,395,385,249,604,375,877,752,938,98,865,277,380,221,408,569,749,293,972,243,668,474,315,931,566,577,474,347,396,647,867,229,141,458,978,752,855,49,822,27,295,332,757,198,368,214,693,885,450,397,821,722,148,397,957,381,190,312,249,171,625,534,507,663,317,356,971,608,247,855,489,719,809,51,197,344,707,716,640,22,138,11,802,461,9,276,920,552,413,942,818,696,495,706,348,556,562,962,988,887,491,720,203,567,533,790,494,351,675,847,55,906,590,578,251,182,148,117,804,122,54,37,260,774,677,61,515,711,15,412,28,917,475,25,483,230,987,673,549,875,642,915,60,176,493,230,913,642,99,339,301,216,51,393,301,609,864,646,956,464,412,526,778,293,247,70,441,870,762,199,670,960,979,629,157,244,513,246,113,803,935,67,827,175,859,734,491,987,314,409,345,89,556,986,194,784,599,853,370,728,613,628,204,730,53,742,854,565,546,150,878,781,393,97,484,816,172,322,295,997,287,568,172,623,852,285,984,156,541,781,881,386,289,671,851,83,634,66,193,195,638,112,682,499,646,840,116,622,349,83,30,289,135,670,878,674,543,377,78,474,293,463,356,976,858,256,261,511,110,152,773,627,132,483,47,855,661,778,209,140,807,96,190,310,861,713,545,2,193,70,189,855,368,758,237,688,592,499,83,927,875,49,838,265,903,1,227,164,942,199,560,978,255,784,79,294,425,138,585,728,406,472,763,169,970,780,538,633,331,286,146,738,233,678,754,825,114,679,447,948,859,475,111,713,482,640,366,960,559,837,57,990,421,100,863,87,985,836,298,424,564,549,784,456,584,461,525,189,108,210,5,745,313,373,283,339,468,501,201,768,823,345,926,786,828,460,633,806,963,180,877,159,109,230,381,352,436,448,912,717,251,90,180,346,247,112,280,928,438,357,771,87,838,329,818,589,231,200,687,727,593,316,773,988,653,796,665,329,236,648,609,319,652,900,842,162,139,541,901,189,774,924,411,855,981,449,275,74,817,261,77,704,415,87,291,921,753,190,907,64,706,306,732,313,532,39,765,389,324,203,348,165,438,447,357,140,570,315,298,251,441,358,87,579,747,311,282,547,562,491,113,465,665,782,271,791,324,377,661,700,516,802,314,764,607,718,382,773,820,301,222,280,342,88,110,478,395,169,213,278,564,481,466,757,596,761,172,512,150,571,615,937,726,371,310,225,282,273,966,261,302,891,857,190,107,811,437,412,669,442,73,590,887,197,309,72,606,470,79,838,686,120,602,831,803,125,155,224,426,77,18,870,186,708,52,611,571,875,405,866,725,319,410,398,206,208,800,574,406,291,827,518,117,259,146,246,971,303,176,375,762,372,746,160,935,142,199,755,935,139,635,55,101,946,565,688,115,129,170,166,989,344,455,942,393,494,97,31,524,258,573,137,31,589,384,307,230,325,102,663,876,691,628,981,209,258,553,502,249,700,872,889,324,387,513,844,644,384,562,69,465,847,517,909,466,92,588,351,678,402,208,961,599,252,980,889,983,758,153,685,948,246,301,465,33,147,135,882,570,154,691,504,659,515,268,711,115,661,858,928,672,529,140,889,156,104,289,717,624,120,989,256,189,554,617,243,253,142,814,314,110,662,625,973,286,573,190,464,860,514,420,83,121,833,249,276,851,971,311,576,560,668,61,994,362,269,812,775,13,689,665,586,847,288,617,875,550,985,996,754,404,917,872,331,405,558,663,721,17,162,240,145,646,438,616,922,293,977,848,105,123,251,400,996,580,743,139,916,741,315,121,157,882,916,181,885,114,35,64,118,744,781,852,22,424,776,740,441,409,3,535,919,457,822,78,376,53,684,685,33,291,29,884,256,426,512,526,268,88,188,242,195,333,781,546,562,50,930,576,892,817,152,689,299,762,402,732,585,837,106,637,691,741,216,660,646,855,266,354,255,331,467,719,550,30,783,500,397,613,362,180,561,723,608,764,871,813,376,137,183,557,986,574,661,21,440,153,55,193,230,393,683,645,5,170,886,29,241,513,259,767,810,545,485,157,744,660,719,312,569,698,469,791,221,821,699,980,568,93,764,934,225,627,860,300,411,265,226,104,687,540,58,251,190,365,629,546,630,38,536,993,549,737,802,72,195,37,838,90,403,444,639,43,755,232,718,515,3,72,402,561,464,969,214,673,175,179,471,82,120,413,351,476,639,576,905,789,804,865,282,916,627,404,731,197,909,496,634,788,384,904,752,29,26,696,370,273,348,758,848,23,730,677,747,643,43,495,64,174,337,408,691,116,98,443,53,844,688,400,985,713,830,859,896,71,40,625,887,911,164,824,428,329,146,900,72,677,292,388,95,323,341,583,89,386,321,968,39,428,78,57,805,357,944,959,842,250,260,590,687,109,176,363,462,249,783,760,52,980,379,85,107,815,900,108,158,339,114,208,866,33,981,318,719,985,648,355,456,965,737,353,625,129,193,598,147,484,783,985,462,938,419,764,600,803,472,973,78,821,439,784,335,665,463,759,91,34,175,917,472,846,264,814,542,759,436,531,894,475,568,932,823,64,762,499,424,190,767,684,114,782,374,159,618,226,269,227,891,146,54,45,783,920,172,211,743,825,864,370,60,463,573,971,879,560,973,182,834,108,600,485,614,911,572,245,104,722,819,341,589,207,777,873,241,713,583,889,295,668,848,906,150,425,418,379,852,778,480,681,299,916,220,160,570,381,829,118,177,661,618,862,338,124,404,270,543,160,851,167,309,580,532,170,958,897,811,828,699,622,286,729,645,975,500,991,414,396,262,392,684,833,605,819,446,679,393,28,453,250,698,636,749,192,703,172,371,996,973,71,226,254,763,822,153,742,814,230,442,409,534,674,774,951,826,64,172,654,680,827,196,861,511,690,233,99,464,817,723,289,184,821,762,871,170,17,115,798,482,999,890,935,352,346,148,874,873,676,56,393,831,160,514,179,30,530,665,812,697,221,543,205,963,454,23,621,12,823,747,564,483,137,296,703,191,856,983,323,508,473,395,283,978,639,359,802,875,206,400,335,648,93,421,685,574,500,362,870,181,388,605,879,624,257,536,836,238,263,858,350,115,568,247,713,146,580,136,972,53,530,676,300,979,20,621,595,161,504,815,826,268,628,927,407,29,843,853,463,521,488,799,70,41,597,279,816,513,344,126,747,818,274,566,440,362,85,406,856,469,384,634,898,643,596,281,164,532,898,260,946,203,874,674,424,880,672,669,131,812,570,51,794,144,406,568,768,501,71,289,558,129,95,360,500,792,840,432,994,300,210,390,692,166,202,135,774,85,256,680,496,120,737,789,802,949,425,844,506,630,409,64,988,528,690,493,241,869,166,201,212,166,935,880,887,164,373,373,153,791,348,632,492,850,454,443,315,945,446,485,221,353,802,550,110,627,225,959,883,280,792,404,826,145,223,773,324,353,378,29,898,787,95,51,955,259,224,546,620,498,572,497,989,658,941,837,685,285,525,876,36,969,611,667,729,576,732,654,902,390,969,30,779,307,228,475,709,654,837,892,335,683,921,499,195,835,46,842,974,611,691,531,155,105,427,877,245,274,573,230,794,940,41,99,649,957,10,541,466,109,137,169,829,116,797,529,781,879,256,352,524,816,683,901,516,877,190,137,353,103,596,127,845,454,313,551,325,130,852,744,51,775,92,660,368,274,777,587,296,106,518,867,949,101,24,56,488,60,665,917,278,499,76,594,859,587,46,481,342,873,401,830,914,647,243,52,934,397,409,419,527,113,992,446,658,182,720,644,59,35,693,911,205,365,318,696,737,100,915,323,150,169,769,491,132,157,792,205,628,203,971,636,490,299,366,100,891,698,139,169,511,806,909,737,890,632,414,234,320,252,501,36,904,144,882,40,637,140,166,167,717,802,512,761,679,427,872,543,546,872,435,935,553,209,461,316,750,586,194,537,419,923,456,715,396,274,891,446,386,433,769,497,137,217,869,931,589,99,863,57,969,277,961,169,164,427,823,132,291,566,673,327,178,713,151,185,390,860,249,77,199,658,240,413,631,415,104,935,33,539,845,107,529,764,270,449,624,326,602,970,651,85,301,128,295,183,180,109,172,938,231,840,454,751,862,726,673,318,911,556,336,316,914,330,447,358,932,53,558,994,133,519,466,283,536,584,337,657,718,762,596,700,303,809,765,49,144,876,920,383,537,244,187,735,186,488,803,591,6,563,376,159,788,116,902,213,957,930,749,312,834,762,118,89,127,861,688,376,456,291,869,63,535,591,717,195,113,516,686,714,53,917,306,43,124,449,311,829,805,155,136,187,501,911,191,984,198,454,702,510,998,812,940,114,260,711,19,887,456,312,386,743,387,212,227,765,762,996,882,370,648,957,410,452,20,829,612,861,363,942,738,743,882,99,600,732,854,477,91,279,968,290,672,548,854,733,491,607,454,42,326,983,309,341,925,526,621,982,677,374,194,109,391,819,244,488,215,719,896,723,301,731,667,425,504,952,771,142,319,262,403,546,626,899,884,446,541,844,248,578,776,249,334,480,561,443,25,594,875,32,633,664,710,82,771,909,799,252,706,99,275,577,313,168,738,264,37,551,524,945,644,474,163,629,574,54,241,193,326,996,192,36,1,682,711,386,725,386,134,181,348,826,547,315,949,806,407,895,607,132,937,262,241,634,986,285,140,350,791,282,757,149,135,954,602,946,11,532,197,498,754,689,277,159,400,169,925,352,812,217,958,775,48,428,120,589,359,346,330,333,11,826,117,70,402,317,134,796,531,230,66,56,737,636,94,687,402,131,494,277,718,876,814,423,735,256,98,399,767,591,224,961,351,29,858,316,441,36,695,487,170,381,540,580,576,90,837,402,76,582,969,443,386,899,187,98,605,232,563,460,493,538,186,632,977,724,476,471,855,207,391,804,692,878,722,834,673,355,246,668,195,251,57,108,472,180,180,736,524,584,914,775,302,592,692,639,552,903,698,641,654,171,480,821,586,170,246,467,304,32,635,573,815,245,320,91,142,604,499,911,949,25,273,792,360,523,99,120,787,738,40,537,288,463,359,6,349,466,651,177,281,119,249,496,809,54,61,604,663,809,777,932,247,540,566,68,317,834,664,248,973,959,744,642,860,981,515,320,278,152,926,467,705,909,884,439,172,843,195,310,173,27,382,356,862,776,737,856,37,62,2,88,839,712,122,569,915,472,145,390,184,676,611,679,804,861,609,655,720,974,442,873,536,97,784,956,694,567,396,709,36,885,621,413,142,405,496,561,890,358,626,508,666,645,363,991,400,508,901,805,225,861,394,247,65,990,916,776,89,874,340,843,754,428,959,648,13,888,416,96,607,321,794,735,327,328,736,891,598,136,782,627,787,269,136,95,299,190,583,68,273,85,458,953,120,872,228,361,935,975,237,98,930,306,336,973,592,864,808,258,329,634,781,1,131,917,92,655,105,644,682,862,869,254,144,377,998,135,249,159,447,207,404,750,325,352,790,391,483,954,231,524,208,638,930,25,401,573,167,654,783,987,956,154,243,727,127,55,666,559,621,97,974,83,678,936,380,539,616,388,750,910,703,313,335,155,87,515,355,315,250,236,643,147,380,948,228,184,437,1,609,596,592,374,822,371,303,831,390,973,651,770,566,277,178,575,546,616,770,21,813,692,919,272,179,884,359,877,864,643,657,910,520,604,44,981,221,558,617,157,193,848,254,581,583,527,68,579,409,829,917,539,436,446,710,117,578,876,831,483,380,269,336,869,636,175,986,258,568,384,132,333,727,243,814,752,809,614,502,485,392,737,560,143,774,733,417,914,212,438,402,547,405,952,11,878,530,251,263,292,356,475,228,972,526,361,881,485,314,554,128,116,888,563,301,701,85,943,121,830,249,715,301,670,116,833,97,404,311,777,927,792,864,390,183,560,58,689,142,759,708,856,997,782,262,752,689,146,407,737,521,8,142,922,14,567,265,910,467,437,891,801,131,769,624,105,920,561,450,370,755,774,487,738,492,596,889,641,800,2,572,674,747,428,415,927,156,662,75,956,800,878,638,96,722,126,80,739,161,833,956,374,114,745,123,82,148,382,189,274,976,85,475,385,15,696,209,286,320,864,940,129,919,717,784,626,698,313,601,642,488,563,903,148,706,647,949,233,231,295,794,657,102,933,657,287,169,185,673,25,149,293,539,800,217,924,979,313,731,518,477,506,683,56,614,781,422,809,849,944,637,220,64,530,131,616,434,655,674,373,431,155,689,979,902,220,617,897,274,805,958,83,39,335,252,792,602,400,231,802,519,972,747,159,547,43,263,590,542,998,434,222,111,747,211,96,906,284,947,811,614,392,410,150,576,595,415,255,9,831,596,958,143,909,582,586,261,880,783,387,736,564,360,382,653,244,60,392,255,158,821,374,470,600,246,173,777,644,50,470,680,594,456,87,877,3,503,309,89,788,277,396,993,25,592,331,196,49,895,256,85,537,317,43,777,809,769,487,792,419,48,68,136,888,839,147,496,602,899,878,166,684,212,84,60,886,426,889,683,993,834,761,870,65,607,532,515,988,117,826,271,385,912,562,520,318,88,461,685,865,683,675,987,779,852,725,643,539,79,945,537,574,417,825,294,323,368,894,366,929,797,470,580,880,901,967,361,117,49,512,216,736,795,338,268,581,32,820,103,323,712,388,402,371,199,178,572,264,533,942,540,912,846,407,945,52,715,59,322,358,409,354,848,178,729,27,955,433,235,267,51,29,559,214,688,483,215,121,136,699,927,476,672,439,514,446,103,163,593,427,128,579,675,139,200,603,522,236,62,187,686,341,347,679,150,639,426,877,77,689,473,466,884,524,217,608,589,744,347,509,364,284,493,8,550,758,179,557,816,942,25,516,629,960,61,228,634,395,851,477,460,10,302,3,561,745,393,807,193,193,243,546,802,292,777,773,559,92,962,628,607,554,106,518,276,288,857,654,333,867,731,511,469,886,316,814,923,9,745,359,3,11,500,755,334,623,907,547,562,264,987,845,878,465,98,465,872,447,287,928,354,560,648,361,303,284,292,428,359,165,509,161,677,281,282,75,15,557,91,159,760,746,953,520,396,254,508,197,218,5,65,667,63,775,914,259,70,446,977,35,74,180,157,498,862,12,873,260,539,350,46,60,998,452,711,229,681,613,705,466,886,260,17,700,195,756,624,233,700,565,622,621,630,413,459,247,438,626,12,898,924,669,219,822,878,677,529,306,587,944,948,542,23,744,256,304,233,421,413,360,80,866,21,785,716,675,207,921,672,684,831,105,476,376,598,305,521,880,73,745,452,84,646,892,151,251,332,26,811,205,944,257,753,990,396,742,931,165,761,682,747,990,452,164,769,875,279,379,715,419,794,603,169,374,116,902,318,183,267,387,715,326,835,150,560,160,254,245,106,38,455,819,189,662,409,471,24,700,802,684,981,699,678,645,717,920,336,324,809,219,22,960,404,275,515,65,690,878,366,972,985,128,387,331,60,460,303,336,809,10,297,815,33,802,263,530,72,794,460,5,226,372,691,139,191,398,499,113,385,41,418,491,326,135,918,268,416,541,815,998,927,707,41,602,461,379,699,666,925,475,830,789,906,757,908,174,431,398,235,928,61,477,171,146,25,1,673,554,790,491,253,844,208,45,346,946,715,804,147,307,154,43,67,742,418,129,402,357,354,322,927,453,563,260,158,831,646,800,186,373,298,213,965,376,336,86,507,319,882,165,506,614,984,919,35,655,635,97,487,459,418,3,585,470,975,532,479,784,53,600,727,586,929,247,929,733,248,125,623,715,707,153,798,403,887,693,300,360,184,198,365,321,821,675,152,665,688,614,157,925,372,211,499,921,809,299,164,644,292,712,167,810,602,200,850,33,395,367,152,332,67,236,637,372,848,650,162,536,244,735,469,181,536,715,258,984,944,978,900,849,748,552,450,107,663,640,606,276,570,21,385,992,798,786,811,157,356,884,166,847,445,282,624,645,871,380,892,854,850,571,517,194,933,677,77,148,412,3,331,12,231,525,861,709,492,982,805,644,37,838,998,662,270,836,556,849,592,711,62,168,85,835,322,750,216,11,678,103,474,289,205,561,622,839,299,306,523,130,298,613,536,727,909,271,725,895,839,983,990,520,543,113,71,709,576,933,950,428,569,504,880,185,182,687,965,35,777,844,900,427,890,307,833,313,438,493,537,6,694,150,106,792,191,259,153,462,590,948,216,673,987,318,663,363,470,858,516,46,136,89,119,308,284,334,863,696,858,440,214,444,4,211,798,262,397,63,456,804,595,253,286,746,558,474,79,591,13,280,141,15,30,691,61,266,87,457,345,196,81,934,54,180,458,773,438,873,525,878,472,977,104,299,647,80,872,68,599,330,963,227,216,578,258,1000,449,569,13,928,3,351,653,988,300,673,92,146,790,104,53,891,321,552,110,445,88,264,314,647,317,746,644,309,320,410,679,190,163,688,407,558,921,576,361,182,372,57,168,873,777,652,7,908,116,475,127,580,15,301,529,561,786,722,191,560,727,149,291,206,38,507,946,137,793,371,671,518,34,151,394,754,271,21,566,41,185,549,309,896,848,78,574,561,845,686,418,124,417,174,27,272,500,777,864,277,952,986,900,571,262,303,85,922,430,458,439,349,287,520,512,698,592,904,493,359,735,719,949,362,232,591,715,612,45,546,779,987,228,916,616,407,976,381,35,794,532,241,290,299,165,443,788,961,599,358,569,284,175,622,550,782,376,743,892,709,889,698,32,524,82,422,79,568,410,789,904,356,230,871,227,845,764,902,872,638,413,450,388,102,303,340,292,841,346,541,186,29,959,875,43,483,3,164,859,882,915,852,802,689,27,193,56,568,676,767,575,164,905,332,598,722,646,99,873,101,523,963,283,657,579,309,122,919,92,866,18,132,560,889,314,3,553,535,991,523,315,111,629,707,539,500,623,664,994,719,38,37,498,401,728,402,247,152,960,742,146,107,521,439,206,281,331,80,506,931,389,960,307,962,403,450,841,400,683,804,829,194,910,84,43,3,553,450,642,937,453,458,274,189,684,789,220,79,31,265,233,774,630,944,899,491,161,399,348,883,531,969,912,538,197,143,730,860,52,132,615,333,206,647,16,293,368,320,188,347,269,880,16,141,44,35,54,780,196,865,796,813,710,238,398,495,198,221,118,216,550,700,291,853,963,812,191,391,642,871,353,63,401,148,529,748,865,77,22,748,30,571,818,435,571,231,898,164,358,845,402,789,635,772,925,459,311,921,874,914,73,838,825,489,58,176,104,640,309,108,262,828,158,300,108,181,985,286,230,163,69,359,773,312,809,437,141,889,973,915,780,987,402,312,201,246,214,243,454,777,503,571,668,318,455,167,448,642,571,438,832,303,423,280,754,234,64,345,906,536,23,106,248,419,626,573,390,941,301,644,321,794,85,269,923,495,619,76,697,507,534,150,279,11,317,835,136,859,530,947,576,201,915,494,6,89,124,899,937,167,149,753,611,933,933,244,238,375,191,611,302,523,418,956,88,942,43,25,384,320,844,442,381,167,143,842,685,214,503,402,706,307,476,617,786,486,991,245,565,718,934,515,954,103,232,385,335,765,596,882,494,313,316,255,629,192,500,160,791,10,872,461,836,760,879,611,184,13,900,826,883,647,484,504,751,462,498,646,62,891,127,574,422,821,256,488,132,780,181,743,771,988,617,390,996,364,839,799,808,935,645,559,661,555,605,145,471,526,56,700,52,758,220,157,28,544,683,740,888,755,10,470,181,856,408,80,247,662,251,741,87,249,26,46,895,715,327,383,740,116,393,901,615,856,350,513,372,953,964,945,968,619,893,602,558,788,372,159,594,126,145,820,261,250,129,227,695,229,318,610,747,944,832,686,305,448,997,95,299,34,420,560,632,810,748,678,807,34,550,685,315,498,337,82,89,121,238,492,810,111,33,308,412,825,595,881,714,862,179,124,517,737,168,454,263,395,326,853,196,728,898,876,49,545,273,94,207,981,446,715,646,295,268,498,663,18,685,137,322,738,467,822,604,432,76,354,733,734,208,796,216,275,382,147,420,919,605,361,8,253,285,166,700,680,566,240,969,266,124,213,773,633,196,528,690,496,329,604,843,856,3,800,865,845,626,335,430,305,901,985,528,448,78,341,711,216,120,647,881,395,965,763,816,632,257,706,136,206,657,583,361,746,732,102,60,891,610,916,81,204,310,842,751,148,933,611,592,147,487,159,852,807,337,915,687,771,56,389,341,935,372,246,243,446,520,981,650,739,630,242,54,13,244,98,71,926,921,872,266,695,338,937,881,927,802,964,407,237,517,867,484,56,550,948,767,107,715,360,551,250,165,208,869,156,330,457,720,114,300,811,587,68,892,623,487,347,412,469,313,618,316,756,363,41,273,707,899,572,866,351,894,643,192,779,208,686,293,543,828,895,659,323,78,455,722,438,11,389,235,234,804,320,565,392,329,944,776,69,352,992,382,595,452,496,607,454,70,251,539,535,647,906,284,483,582,56,271,121,143,104,565,545,67,200,52,215,646,459,973,784,136,950,386,331,837,119,821,408,444,699,216,252,32,930,154,907,934,215,587,293,938,796,347,92,847,167,957,963,366,143,813,153,708,751,936,300,619,847,150,796,788,992,735,970,595,878,660,127,430,77,458,341,878,979,377,238,593,936,692,206,499,125,96,915,144,471,229,869,505,763,792,648,620,153,827,879,643,843,41,342,618,88,94,822,405,159,336,867,389,451,679,810,360,778,823,537,574,832,397,341,691,91,783,810,869,627,130,28,153,378,510,666,474,11,948,222,240,663,329,211,473,427,830,344,218,371,992,832,435,654,8,128,42,780,101,392,799,859,446,610,701,918,333,769,459,577,327,635,250,330,438,121,59,787,319,664,74,817,732,861,516,985,170,842,17,840,114,651,364,373,563,41,833,939,496,173,652,885,243,416,697,667,387,462,209,171,379,767,256,250,435,889,801,573,885,818,165,683,508,954,242,648,333,383,453,953,981,676,894,451,268,453,715,410,307,866,812,743,955,341,233,995,338,804,756,318,997,538,653,739,331,62,2,235,639,182,949,215,696,471,507,755,630,928,480,838,679,701,244,890,712,578,344,157,471,94,465,192,194,857,266,686,857,363,326,527,37,181,601,141,249,797,249,509,819,319,50,452,328,418,620,943,99,149,245,118,212,187,911,241,10,820,960,334,4,622,600,207,764,313,502,311,232,421,1,505,982,49,740,875,745,493,855,30,433,414,568,120,201,804,744,265,336,769,212,671,154,955,695,135,967,229,776,327,549,627,267,209,384,344,597,179,788,616,727,924,192,355,961,860,258,551,765,165,240,751,249,294,828,765,601,629,486,207,316,742,991,451,98,1000,712,807,661,633,266,387,36,563,433,296,485,257,514,852,389,661,993,906,200,309,141,382,224,509,538,653,566,224,174,172,725,11,657,993,355,930,776,757,867,715,505,597,814,381,175,702,296,651,159,485,821,486,318,329,921,900,46,997,87,321,149,293,823,341,463,541,285,456,755,456,539,984,933,961,509,237,888,882,509,258,82,824,75,126,727,537,497,482,209,954,276,192,565,474,71,365,618,577,412,720,718,329,26,138,766,327,370,815,287,477,12,721,760,393,633,759,529,232,361,66,595,390,516,266,19,597,180,233,591,963,680,80,264,333,33,786,434,662,892,821,27,649,915,774,385,820,347,912,91,61,541,651,465,475,374,909,430,251,663,750,513,466,800,908,519,612,476,629,921,336,272,997,242,687,664,466,935,73,346,146,89,525,438])

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1: return 0

        dp = [0] * len(nums)
        remainingInJump = 0

        for i in range(len(nums)):
            if nums[i] > remainingInJump:
                tempMax = nums[i] + 1
                tempSub = remainingInJump
                for k in range(tempSub, tempMax):
                    if i + k < len(nums) and not dp[i + k]:
                        dp[i + k] = dp[i] + 1
                remainingInJump = nums[i] - 1
            else:
                remainingInJump = remainingInJump - 1

        # print(dp)
        return dp[-1] - 1

    def jumpOld(self, nums: List[int]) -> int:

        if len(nums) == 1: return 0

        dp = [0] * len(nums)
        remainingInJump = 0

        for i in range(len(nums)):
            if nums[i] > remainingInJump:
                tempMax = nums[i] + 1
                tempSub = remainingInJump
                for k in range(tempSub, tempMax):
                    if i + k < len(nums) and not dp[i + k]:
                        dp[i + k] = dp[i] + 1
                remainingInJump = nums[i] - 1
            else:
                remainingInJump = remainingInJump - 1

        print(dp)
        return dp[-1] - 1

    def jump99of106(self, nums: List[int]) -> int:

        if len(nums) == 1: return 0

        dp = [0] * len(nums)
        remainingInJump = nums[0]

        for i in range(len(nums)):

            # Set the forward jumps to the current num first
            for j in range(1, remainingInJump + 1):
                if j < len(nums) and not dp[j]:
                    dp[j] = dp[i] + 1

            if nums[i] > remainingInJump:
                #
                tempMax = nums[i] + 1
                tempSub = remainingInJump
                for k in range(tempSub, tempMax):
                    if i + k < len(nums) and not dp[i + k]:
                        dp[i + k] = dp[i] + 1

            remainingInJump = remainingInJump - 1

        print(dp)
        return dp[-1]

    def jump2(self, nums: List[int]) -> int:

        if len(nums) == 1: return 0

        dp = [0] * len(nums)
        currentJumpCounter = nums[0]
        # numJumps = 1

        nextUnreachedIndex = 1

        for i in range(len(nums)):

            # Set the forward jumps to the current num first
            if i < nextUnreachedIndex:
                for j in range(1, currentJumpCounter + 1):
                    if j < len(nums) and not dp[j]:
                        dp[j] = dp[i] + 1
                        nextUnreachedIndex += 1

            if nums[i] > currentJumpCounter:
                #
                tempMax = nums[i]
                tempSub = currentJumpCounter - 1
                for k in range(currentJumpCounter - 1, tempMax):
                    if i + k < len(nums) and not dp[i + k]:
                        dp[i + k] = dp[i] + 1
                        nextUnreachedIndex += 1
                # currentJumpCounter = max(currentJumpCounter, nums[i])
                # dp[i] = currentJumpCounter

            currentJumpCounter = currentJumpCounter - 1

        print(dp)
        return dp[-1]


if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()

class Solution:
    def maxSatisfaction( satisfaction: list[int]) -> int:
        # mx = sum(satisfaction)
        # print("this is the first ",mx)
        # org = sorted(satisfaction)
        # satisfaction = org.copy()
        # if any(num < 0 for num in satisfaction):
        #     while  any(num < 0 for num in satisfaction):
        #         for i in range(1,len(satisfaction)+1):
        #             satisfaction[i-1]*=i
        #         sm = sum(satisfaction)
        #         if sm>mx:
        #             mx = sm
        #         org.pop(satisfaction.index(min(satisfaction)))
        #         satisfaction = org.copy()
        #         print(mx)
        # else:
        #     for i in range(1,len(satisfaction)+1):
        #         mx +=satisfaction[i-1]*i
        # print(satisfaction,sum(satisfaction))
        # return mx,mx+sum(satisfaction)
        satisfaction.sort() 
        max_sum = 0  
        total_time = 0 
        for i in range(len(satisfaction) - 1, -1, -1):
            if satisfaction[i] + total_time > 0:
                total_time += satisfaction[i]
                max_sum += total_time
        return max_sum
    print(maxSatisfaction(satisfaction = [-503, -384, 190, -152, -459, -20, -21, 307, 653, 311, 846, 600, -632, 62, 143, 888, -323, -557, -169, -957, 689, -622, 159, -796, -146, -896, 238, 512, -122, -973, 840, 796, -767, 980, -487, 451, -14, 77, -867, 802, 505, -158, -725, 656, -266, -119, -924, 428, -780, -104, -446, 635, -428, -922, -888, -131, -830, -831, -479, 219, 403, 859, 426, 716, -791, -690, 617, -126, -607, 843, -573, -689, -411, -897, 1, 148, -436, -983, -217, -38, 697, 707, -679, -213, 902, -866, -490, 137, -386, 397, -510, 837, 135, 536, -582, 356, -98, 163, 589, -926, 654, -631, -249, -183, 535, 879, -90, 757, -232, 675, 917, -35, -623, -692, 85, -139, 738, -107, 492, 252, -646, -466, -793, 647, 320, -215, -351, 537, 916, -721, -516, -675, -867, 968, 573, -108, 910, -182, 733, -796, -840, 178, 245, -187, 904, -522, 227, -207, -470, 603, -438, 834, 809, -506, -750, 143, -369, -913, 736, 262, -796, 188, 186, -772, -223, -486, 647, -739, -229, -147, -98, 517, 802, 61, 753, -260, 842, -467, 993, -492, -906, 872, -612, -171, -55, 596, 747, 389, -255, -728, -637, -831, -598, 18, 107, 970, 664, -110, 613, 82, 672, -505, 935, -544, 760, 621, -481, -410, -499, -652, -458, 957, -809, -864, -823, -12, 804, 574, -953, 654, -385, 397, -92, 523, -450, 121, 648, -833, -803, 863, -492, -961, 658, -660, -529, 751, 256, 381, -387, -533, 642, -572, -604, -961, 300, -873, 575, -640, 701, -568, -418, -805, -300, -473, 697, 235, -779, -466, -561, -685, -145, -800, 199, -639, 215, -932, -200, 166, -19, 251, 902, -116, -546, -897, -347, -938, -168, -60, 879, 148, 494, -760, 604, -311, 289, -685, 647, -304, 17, 721, -70, 590, 177, -369, 765, -320, 462, -567, -369, 288, 323, -102, 407, 569, 16, 757, -788, -556, -984, -343, 739, 260, -683, 325, 175, -896, 486, 22, 326, 974, -868, -218, -902, -7, 244, -341, -197, -959, 487, -766, 419, -420, -683, -759, -618, 394, -651, -198, -469, -469, 484, 436, 876, 98, -815, 71, 330, 440, 909, -642, -311, -326, 644, 358, -956, -182, -768, -15, 918, 962, 558, -486, -753, 254, 216, -272, -469, 717, 658, -325, 446, -194, -577, -28, -918, -122, -378, -231, -699, 0, -607, 211, -831, -423, 520, -358, 747, 165, -71, 15, -893, 727, -671, -861, 338, 823, 639, 668, -731, 606, -335, 295, -248, 792, 641, -311, 329, -536, 243, -293, 485, 45, -784, -890, 929, 611, -165, 154, 786, 688, -180, -392, -88, 649, -80, 94, -151, 857, 664, -882, 185, 268, -676, 478, 288, -384, -455, 87, 352, 908, -515, 812, 924, -838, 639, 649, 483, 288, 354, 124, -723, -112, 338, 965, -443, 743, 443, 537, 706, 940, -666, 296, 629, -223, -898, 191, 468, 944, 875, -219, -148, 97, 994, -29, 817, -853, -810, 10, -535, 899, 22, 680, -410, -540, -896, 652, -946, 4, -133, -308, -540, 22, 161, -276, -197, -652, -290, -354, -416, -760]))
# from random import randint
# print([randint(-1000, 1000) for i in range(500)])
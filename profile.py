import requests
from bs4 import BeautifulSoup
import pandas as pd
from deep_translator import GoogleTranslator
import time

translator = GoogleTranslator(source='auto', target='en')

baseUrl = 'https://www.dragonvillage.net/dv1/info/dragoninfo?mode=read&'

def main():
    d_nos = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
        64,
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        97,
        98,
        99,
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        115,
        116,
        117,
        118,
        119,
        120,
        121,
        122,
        123,
        124,
        125,
        126,
        127,
        128,
        129,
        130,
        131,
        132,
        133,
        134,
        135,
        136,
        137,
        138,
        139,
        140,
        141,
        142,
        143,
        144,
        145,
        146,
        147,
        148,
        149,
        150,
        151,
        152,
        153,
        154,
        167,
        168,
        169,
        170,
        171,
        172,
        173,
        174,
        175,
        176,
        177,
        178,
        179,
        180,
        181,
        182,
        183,
        184,
        185,
        186,
        187,
        188,
        189,
        190,
        191,
        192,
        193,
        194,
        195,
        196,
        197,
        198,
        199,
        200,
        201,
        202,
        203,
        204,
        205,
        206,
        207,
        208,
        209,
        210,
        211,
        212,
        213,
        214,
        215,
        216,
        217,
        218,
        219,
        220,
        221,
        222,
        223,
        224,
        225,
        226,
        227,
        228,
        229,
        230,
        231,
        232,
        233,
        234,
        235,
        236,
        237,
        238,
        239,
        240,
        241,
        242,
        243,
        244,
        245,
        246,
        247,
        248,
        249,
        250,
        251,
        252,
        253,
        254,
        255,
        256,
        257,
        258,
        259,
        260,
        261,
        262,
        263,
        264,
        265,
        266,
        267,
        268,
        269,
        270,
        271,
        272,
        273,
        274,
        275,
        276,
        277,
        278,
        279,
        280,
        281,
        282,
        283,
        284,
        285,
        286,
        287,
        288,
        289,
        290,
        291,
        292,
        293,
        294,
        295,
        296,
        297,
        298,
        299,
        300,
        301,
        302,
        303,
        304,
        305,
        306,
        307,
        308,
        309,
        310,
        311,
        312,
        313,
        314,
        315,
        316,
        317,
        318,
        319,
        320,
        321,
        322,
        323,
        324,
        325,
        326,
        327,
        328,
        329,
        330,
        331,
        332,
        333,
        334,
        335,
        336,
        337,
        338,
        339,
        340,
        341,
        342,
        343,
        344,
        345,
        346,
        347,
        348,
        349,
        350,
        351,
        352,
        353,
        354,
        355,
        356,
        357,
        358,
        359,
        360,
        361,
        362,
        363,
        364,
        365,
        366,
        367,
        368,
        369,
        370,
        371,
        372,
        373,
        374,
        375,
        376,
        377,
        378,
        379,
        380,
        381,
        382,
        383,
        384,
        385,
        386,
        387,
        388,
        389,
        390,
        391,
        392,
        393,
        394,
        395,
        396,
        397,
        398,
        399,
        400,
        401,
        402,
        403,
        404,
        405,
        406,
        407,
        408,
        409,
        410,
        411,
        412,
        413,
        414,
        415,
        416,
        417,
        418,
        419,
        420,
        421,
        422,
        423,
        424,
        425,
        426,
        427,
        428,
        429,
        430,
        431,
        432,
        433,
        434,
        435,
        436,
        437,
        438,
        439,
        440,
        441,
        442,
        443,
        444,
        445,
        446,
        447,
        448,
        449,
        450,
        451,
        452,
        453,
        454,
        455,
        456,
        457,
        458,
        459,
        460,
        461,
        462,
        463,
        464,
        465,
        466,
        467,
        468,
        469,
        470,
        475,
        476,
        477,
        478,
        479,
        480,
        481,
        482,
        483,
        484,
        485,
        486,
        487,
        488,
        489,
        491,
        492,
        493,
        494,
        495,
        496,
        501,
        502,
        503,
        504,
        505,
        506,
        507,
        508,
        509,
        510,
        511,
        512,
        513,
        514,
        515,
        516,
        517,
        518,
        519,
        520,
        521,
        522,
        523,
        524,
        525,
        526,
        527,
        528,
        529,
        530,
        531,
        532,
        533,
        534,
        535,
        536,
        537,
        538,
        539,
        540,
        541,
        542,
        543,
        544,
        545,
        546,
        547,
        548,
        549,
        551,
        552,
        553,
        554,
        555,
        556,
        557,
        558,
        559,
        560,
        561,
        562,
        563,
        564,
        565,
        566,
        567,
        568,
        569,
        570,
        571,
        572,
        573,
        574,
        575,
        576,
        577,
        578,
        579,
        580,
        581,
        582,
        583,
        584,
        585,
        586,
        587,
        588,
        589,
        590,
        591,
        592,
        593,
        594,
        595,
        596,
        597,
        598,
        599,
        600,
        601,
        602,
        603,
        604,
        605,
        606,
        607,
        608,
        609,
        610,
        611,
        612,
        613,
        614,
        615,
        616,
        617,
        618,
        619,
        620,
        621,
        622,
        623,
        624,
        625,
        626,
        627,
        628,
        629,
        630,
        631,
        632,
        633,
        634,
        635,
        636,
        637,
        638,
        639,
        640,
        641,
        642,
        643,
        644,
        645,
        646,
        647,
        648,
        649,
        650,
        651,
        652,
        653,
        654,
        655,
        656,
        657,
        658,
        659,
        660,
        661,
        662,
        663,
        664,
        665,
        666,
        667,
        668,
        669,
        670,
        671,
        672,
        673,
        674,
        675,
        676,
        677,
        678,
        679,
        680,
        681,
        682,
        683,
        684,
        685,
        686,
        687,
        688,
        689,
        690,
        691,
        692,
        693,
        694,
        695,
        696,
        697,
        698,
        699,
        700,
        701,
        702,
        703,
        704,
        705,
        706,
        707,
        708,
        709,
        710,
        711,
        712,
        713,
        714,
        715,
        716,
        717,
        718,
        719,
        720,
        721,
        722,
        723,
        724,
        725,
        726,
        727,
        728,
        729,
        730,
        731,
        732,
        733,
        734,
        735,
        736,
        737,
        738,
        739,
        740,
        741,
        742,
        743,
        744,
        745,
        746,
        747,
        748,
        749,
        750,
        751,
        752,
        753,
        754,
        755,
        756,
        757,
        758,
        759,
        760,
        761,
        762,
        763,
        764,
        765,
        766,
        767,
        768,
        769,
        770,
        771,
        772,
        773,
        774,
        775,
        776,
        777,
        778,
        779,
        780,
        781,
        782,
        783,
        784,
        785,
        786,
        787,
        788,
        789,
        790,
        791,
        792,
        793,
        794,
        795,
        796,
        797,
        798,
        799,
        800,
        801,
        802,
        803,
        804,
        805,
        806,
        807,
        808,
        809,
        810,
        811,
        812,
        813,
        814,
        815,
        816,
        817,
        818,
        819,
        820,
        821,
        822,
        823,
        824,
        825,
        826,
        827,
        828,
        829,
        830,
        831,
        832,
        833,
        834,
        835,
        836,
        837,
        838,
        839,
        840,
        841,
        842,
        843,
        844,
        845,
        846,
        847,
        848,
        849,
        850,
        851,
        852,
        853,
        854,
        855,
        856,
        857,
        858,
        859,
        860,
        861,
        862,
        863,
        864,
        865,
        866,
        867,
        868,
        869,
        870,
        871,
        872,
        873,
        874,
        875,
        876,
        877,
        878,
        879,
        880,
        881,
        882,
        883,
        884,
        885,
        886,
        887,
        888,
        889,
        890,
        891,
        892,
        893,
        894,
        895,
        896,
        897,
        898,
        899,
        900,
        901,
        902,
        903,
        904,
        905,
        906,
        907,
        908,
        909,
        910,
        911,
        912,
        913,
        914,
        915,
        916,
        917,
        918,
        919,
        920,
        921,
        922,
        923,
        924,
        925,
        926,
        927,
        928,
        929,
        930,
        931,
        932,
        933,
        934,
        935,
        936,
        937,
        938,
        939,
        940,
        941,
        942,
        943,
        944,
        945,
        946,
        947,
        948,
        949,
        950,
        951,
        952,
        953,
        954,
        955,
        956,
        957,
        958,
        959,
        960,
        961,
        962,
        963,
        964,
        965,
        966,
        967,
        968,
        969,
        970,
        971,
        972,
        973,
        974,
        975,
        976,
        977,
        978,
        979,
        980,
        981,
        982,
        983,
        984,
        985,
        986,
        987,
        988,
        989,
        990,
        1005,
        1018,
        1023,
        1030,
        1031,
        1032,
        1033,
        1034,
        1042,
        1043,
        1044,
        1045,
        1046,
        1047,
        1048,
        1049,
        1050,
        1051,
        1052,
        1053,
        1055,
        1056,
        1057,
        1058,
        1059,
        1060,
        1062,
        1063,
        1065,
        1066,
        1067,
        1069,
        1071,
        1072,
        1073,
        1074,
        1075,
        1076,
        2001,
        2002,
        2005,
        2018,
        2030,
        2031,
        2032,
        2033,
        2035,
        2036,
        2037,
        2038,
        2039,
        2040,
        2041,
        2042,
        2050,
        2051,
        2052,
        2054,
        2057,
        2058,
        2059,
        2061,
        2062,
        2063,
        2064,
        2065,
        2067,
        2068,
        2070,
        2071,
        2073,
        2074,
        2075,
        2076,
        2077,
        3001,
        3002,
        3003,
        3004,
        3005,
        3006,
        3007,
        3008,
        3009,
        3010,
        3011,
        3012,
        3013,
        3014,
        3015,
        3016,
        3017,
        3018,
        3019,
        3020,
        3021,
        3022,
        3023,
        3024,
        3025,
        3026,
        3027,
        3028,
        3029,
        3030,
        3031,
        3032,
        3033,
        3034,
        3035,
        3036,
        3037,
        3038,
        3039,
        3040,
        3041,
        3042,
        3043,
        3044,
        3045,
        3046,
        3047,
        3048,
        3049,
        3050,
        3051,
        3052,
        3053,
        3054,
        3055,
        3056,
        3057,
        3058,
        3059,
        3060,
        3061,
        3062,
        3063,
        3064,
        3065,
        3066,
        3067,
        3068,
        3069,
        3070,
        3072,
        3073,
        3074,
        3075,
        3076,
        3077,
        3078,
        3079,
        3080,
        3081,
        3082,
        3084,
        10001,
        10005,
        10043,
        10046,
        15018,
        15044,
        15061,
        15068,
        20032,
        20042,
        20053,
        20063,
        20064,
        25031,
        25034,
        35003,
        35012,
        35022,
        35025,
        35032,
        35045,
        35084,
        35088,
    ]

    for d_no in d_nos:
        steps = [0, 4, 5, 6, 7]

        for step in steps:
            url = baseUrl + 'd_no=%s' % d_no + '&step=%s' % step

            page = requests.get(url)

            # check if page exist
            if page.status_code == 200:
                soup = BeautifulSoup(page.content, 'html.parser')
                info_body = soup.find('div', { 'class': 'info_body' })
                info_body_ul = info_body.find('ul')

                dragon_info = dict()
                dragon_info['id'] = d_no

                # get dragon property
                data = []
                for li in info_body_ul.find_all('li'):
                    trans = translator.translate(str(li.text))
                    li_trans = trans.partition(':')[2] if li.text else ''
                    data.append(li_trans.strip())

                props = ['element', 'type', 'gen', 'step']

                dragon_info.update(dict(zip(props, data)))
                # print(dragon_info)

                table = soup.find_all('table')
                tr = table[1].find_all('tr')

                # populating dragons stats
                stats = []
                for row in tr[2:]:
                    for td in row.find_all('td'):
                        stats.append(td.text)

                stats_label = [
                    'min_lvl_min_atk',
                    'min_lvl_max_atk',
                    'max_lvl_min_atk',
                    'max_lvl_max_atk',
                    'min_lvl_min_def',
                    'min_lvl_max_def',
                    'max_lvl_min_def',
                    'max_lvl_max_def',
                    'min_lvl_min_hp',
                    'min_lvl_max_hp',
                    'max_lvl_min_hp',
                    'max_lvl_max_hp',
                ]

                dragon_info.update(dict(zip(stats_label, stats)))
                print(dragon_info)

                df = pd.DataFrame(dragon_info, columns=[
                    'id',
                    'element',
                    'type',
                    'gen',
                    'step',
                    'min_lvl_min_atk',
                    'min_lvl_max_atk',
                    'max_lvl_min_atk',
                    'max_lvl_max_atk',
                    'min_lvl_min_def',
                    'min_lvl_max_def',
                    'max_lvl_min_def',
                    'max_lvl_max_def',
                    'min_lvl_min_hp',
                    'min_lvl_max_hp',
                    'max_lvl_min_hp',
                    'max_lvl_max_hp'],
                    index=['id']
                )

                with open('dragon info.csv', 'a') as f:
                    df.to_csv(f, header=f.tell() == 0)

                time.sleep(3)

            else:
                pass

main()
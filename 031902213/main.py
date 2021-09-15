import time
import pypinyin
import sys
import psutil
import os

zimubiao=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chazi={
  "卧": "臣卜",
  "项": "工页",
  "功": "工力",
  "攻": "工攵",
  "荆": "茾刂",
  "邪": "牙阝",
  "雅": "牙隹",
  "期": "其月",
  "欺": "其欠",
  "斯": "其斤",
  "鞭": "革便",
  "勒": "革力",
  "划": "戈刂",
  "敬": "苟攵",
  "鹳": "雚鸟",
  "欧": "区欠",
  "切": "七刀",
  "鞋": "革圭",
  "鄞": "堇阝",
  "勤": "堇力",
  "陌": "阝百",
  "陈": "阝东",
  "隐": "阝急",
  "降": "阝夅",
  "队": "阝人",
  "防": "阝方",
  "院": "阝完",
  "阳": "阝日",
  "际": "阝示",
  "阴": "阝月",
  "除": "阝余",
  "险": "阝佥",
  "隔": "阝鬲",
  "障": "阝章",
  "阶": "阝介",
  "陀": "阝它",
  "阵": "阝车",
  "阿": "阝可",
  "隘": "阝益",
  "陵": "阝夌",
  "陷": "阝臽",
  "陶": "阝匋",
  "陪": "阝咅",
  "陕": "阝夹",
  "陆": "阝击",
  "阻": "阝且",
  "孙": "子小",
  "孔": "子乚",
  "孩": "子亥",
  "孤": "子瓜",
  "职": "耳只",
  "聩": "耳贵",
  "聘": "耳甹",
  "取": "耳又",
  "聊": "耳卯",
  "聪": "耳总",
  "耻": "耳止",
  "联": "耳关",
  "聆": "耳令",
  "耿": "耳火",
  "耽": "耳冘",
  "预": "予页",
  "豫": "予象",
  "双": "又又",
  "对": "又寸",
  "戏": "又戈",
  "欢": "又欠",
  "观": "又见",
  "难": "又隹",
  "鸡": "又鸟",
  "艰": "又艮",
  "驻": "马主",
  "骚": "马蚤",
  "驯": "马川",
  "骆": "马各",
  "骑": "马奇",
  "驱": "马区",
  "驰": "马也",
  "骇": "马亥",
  "驶": "马史",
  "验": "马佥",
  "骏": "马夋",
  "骄": "马乔",
  "驴": "马户",
  "骤": "马聚",
  "驳": "马爻",
  "胡": "古月",
  "故": "古攵",
  "鸪": "古鸟",
  "郁": "有阝",
  "耐": "而寸",
  "肆": "镸聿",
  "雄": "厷隹",
  "励": "厉力",
  "耗": "耒毛",
  "艳": "丰色",
  "耕": "耒井",
  "确": "石角",
  "破": "石皮",
  "础": "石出",
  "碑": "石卑",
  "研": "石开",
  "碎": "石卒",
  "碾": "石展",
  "硕": "石页",
  "磁": "石兹",
  "碟": "石枼",
  "砸": "石匝",
  "碌": "石录",
  "砖": "石专",
  "碗": "石宛",
  "砰": "石平",
  "磕": "石盍",
  "硬": "石更",
  "砍": "石欠",
  "碰": "石並",
  "码": "石马",
  "砌": "石切",
  "彩": "采彡",
  "乳": "孚乚",
  "须": "彡页",
  "助": "且力",
  "肢": "月支",
  "朦": "月蒙",
  "鹏": "月月鸟",
  "脱": "月兑",
  "朋": "月月",
  "胜": "月生",
  "股": "月殳",
  "脚": "月去卩",
  "腊": "月昔",
  "腋": "月夜",
  "脉": "月永",
  "胸": "月匈",
  "脂": "月旨",
  "肤": "月夫",
  "脾": "月卑",
  "脆": "月危",
  "胆": "月旦",
  "肚": "月土",
  "脏": "月庄",
  "膀": "月旁",
  "脖": "月孛",
  "胖": "月半",
  "膛": "月堂",
  "腕": "月宛",
  "膊": "月尃",
  "肝": "月干",
  "腮": "月思",
  "胀": "月长",
  "腻": "月贰",
  "肪": "月方",
  "膝": "月桼",
  "脯": "月甫",
  "胱": "月光",
  "腰": "月要",
  "腺": "月泉",
  "肋": "月力",
  "肥": "月巴",
  "腹": "月复",
  "臊": "月喿",
  "胶": "月交",
  "腴": "月臾",
  "肿": "月中",
  "膨": "月彭",
  "胳": "月各",
  "脬": "月孚",
  "肌": "月几",
  "胴": "月同",
  "脐": "月齐",
  "胎": "月台",
  "膜": "月莫",
  "肛": "月工",
  "肮": "月亢",
  "献": "南犬",
  "韬": "韦舀",
  "懿": "壹恣",
  "都": "者阝",
  "鼓": "壴支",
  "颠": "真页",
  "趣": "走取",
  "起": "走已",
  "颉": "吉页",
  "动": "云力",
  "劫": "去力",
  "顽": "元页",
  "魂": "云鬼",
  "协": "十办",
  "赫": "赤赤",
  "博": "十尃",
  "却": "去卩",
  "救": "求攵",
  "教": "孝攵",
  "刊": "干刂",
  "勃": "孛力",
  "规": "夫见",
  "封": "圭寸",
  "卦": "圭卜",
  "埋": "土里",
  "址": "土止",
  "堪": "土甚",
  "堤": "土是",
  "坯": "土丕",
  "坟": "土文",
  "城": "土成",
  "垢": "土后",
  "坝": "土贝",
  "坪": "土平",
  "坎": "土欠",
  "垮": "土夸",
  "坏": "土不",
  "地": "土也",
  "境": "土竟",
  "坛": "土云",
  "坡": "土皮",
  "块": "土夬",
  "坦": "土旦",
  "堆": "土隹",
  "域": "土或",
  "填": "土真",
  "增": "土曾",
  "塔": "土荅",
  "垃": "土立",
  "圾": "土及",
  "圳": "土川",
  "埃": "土矣",
  "墙": "土啬",
  "堵": "土者",
  "均": "土匀",
  "坂": "土反",
  "壤": "土襄",
  "静": "青争",
  "靓": "青见",
  "颊": "夹页",
  "鹉": "武鸟",
  "殉": "歹旬",
  "歼": "歹千",
  "鹂": "丽鸟",
  "敕": "束攵",
  "敷": "旉攵",
  "到": "至刂",
  "邳": "丕阝",
  "融": "鬲虫",
  "刺": "朿刂",
  "赖": "束负",
  "致": "至攵",
  "政": "正攵",
  "殊": "歹朱",
  "殁": "歹殳",
  "殃": "歹央",
  "殓": "歹佥",
  "殒": "歹员",
  "刑": "开刂",
  "副": "畐刂",
  "斑": "玟王",
  "璨": "王粲",
  "现": "王见",
  "环": "王不",
  "理": "王里",
  "球": "王求",
  "珊": "王册",
  "璀": "王崔",
  "玩": "王元",
  "瑄": "王宣",
  "琅": "王良",
  "瑞": "王耑",
  "玻": "王皮",
  "璃": "王离",
  "琢": "王豖",
  "珠": "王朱",
  "玛": "王马",
  "瑜": "王俞",
  "此": "止匕",
  "歧": "止支",
  "颇": "皮页",
  "雌": "此隹",
  "龄": "齿令",
  "战": "占戈",
  "旧": "丨日",
  "频": "步页",
  "眼": "目艮",
  "眦": "目此",
  "睛": "目青",
  "睐": "目来",
  "瞬": "目舜",
  "盼": "目分",
  "眺": "目兆",
  "瞑": "目冥",
  "眶": "目匡",
  "眩": "目玄",
  "睡": "目垂",
  "眨": "目乏",
  "睫": "目疌",
  "眠": "目民",
  "瞄": "目苗",
  "瞪": "目登",
  "睬": "目采",
  "盯": "目丁",
  "睨": "目兒",
  "瞰": "目敢",
  "眯": "目米",
  "睹": "目者",
  "睁": "目争",
  "睦": "目坴",
  "眸": "目牟",
  "瞧": "目焦",
  "瞎": "目害",
  "雎": "目隹",
  "敞": "尚攵",
  "辉": "光军",
  "削": "肖刂",
  "淋": "沐木",
  "滩": "汉隹",
  "没": "氵殳",
  "消": "氵肖",
  "润": "氵闰",
  "清": "氵青",
  "江": "氵工",
  "涛": "氵寿",
  "汪": "氵王",
  "海": "氵每",
  "洋": "氵羊",
  "洁": "氵吉",
  "洗": "氵先",
  "波": "氵皮",
  "深": "氵罙",
  "法": "氵去",
  "津": "氵聿",
  "测": "氵则",
  "泄": "氵世",
  "漫": "氵曼",
  "汉": "氵又",
  "泛": "氵乏",
  "游": "氵斿",
  "汁": "氵十",
  "溯": "氵朔",
  "混": "氵昆",
  "漆": "氵桼",
  "沼": "氵召",
  "汇": "氵匚",
  "源": "氵原",
  "泡": "氵包",
  "滋": "氵兹",
  "浅": "氵戋",
  "溅": "氵贱",
  "沙": "氵少",
  "涵": "氵函",
  "沟": "氵勾",
  "洵": "氵旬",
  "淆": "氵肴",
  "浪": "氵良",
  "澳": "氵奥",
  "湾": "氵弯",
  "港": "氵巷",
  "汽": "氵气",
  "漏": "氵屚",
  "洞": "氵同",
  "浑": "氵军",
  "浏": "氵刘",
  "沉": "氵冗",
  "池": "氵也",
  "滤": "氵虑",
  "漂": "氵票",
  "淡": "氵炎",
  "浙": "氵折",
  "淀": "氵定",
  "涧": "氵间",
  "泊": "氵白",
  "溢": "氵益",
  "滴": "氵啇",
  "渺": "氵目少",
  "温": "氵昷",
  "涂": "氵余",
  "灌": "氵雚",
  "淇": "氵其",
  "污": "氵亏",
  "湿": "氵显",
  "沪": "氵户",
  "滥": "氵监",
  "治": "氵台",
  "潮": "氵朝",
  "潜": "氵替",
  "沈": "氵冘",
  "演": "氵寅",
  "汗": "氵干",
  "漓": "氵离",
  "浇": "氵尧",
  "淮": "氵隹",
  "泻": "氵写",
  "漠": "氵莫",
  "浓": "氵农",
  "潇": "氵萧",
  "洒": "氵西",
  "浮": "氵孚",
  "泓": "氵弘",
  "涟": "氵连",
  "漪": "氵猗",
  "泪": "氵目",
  "渴": "氵曷",
  "沾": "氵占",
  "渗": "氵参",
  "涔": "氵岑",
  "泣": "氵立",
  "渔": "氵鱼",
  "浃": "氵夹",
  "油": "氵由",
  "滑": "氵骨",
  "液": "氵夜",
  "沧": "氵仓",
  "沌": "氵屯",
  "淑": "氵叔",
  "澡": "氵喿",
  "渍": "氵责",
  "洲": "氵州",
  "溜": "氵留",
  "泌": "氵必",
  "沸": "氵弗",
  "潦": "氵尞",
  "沦": "氵仑",
  "洛": "氵各",
  "沛": "氵巿",
  "涌": "氵甬",
  "泚": "氵此",
  "沫": "氵末",
  "涕": "氵弟",
  "涯": "氵厓",
  "涎": "氵延",
  "淌": "氵尚",
  "汹": "氵凶",
  "河": "氵可",
  "滚": "氵衮",
  "酒": "氵酉",
  "渐": "氵斩",
  "洪": "氵共",
  "汜": "氵巳",
  "活": "氵舌",
  "渭": "氵胃",
  "涨": "氵张",
  "溃": "氵贵",
  "浦": "氵甫",
  "沃": "氵夭",
  "涉": "氵步",
  "淝": "氵肥",
  "湖": "氵胡",
  "渡": "氵度",
  "沮": "氵且",
  "浩": "氵告",
  "淹": "氵奄",
  "漉": "氵鹿",
  "沐": "氵木",
  "浴": "氵谷",
  "淳": "氵享",
  "涣": "氵奂",
  "泥": "氵尼",
  "涸": "氵固",
  "济": "氵齐",
  "滞": "氵带",
  "澄": "氵登",
  "颗": "果页",
  "歇": "曷欠",
  "昭": "日召",
  "时": "日寸",
  "曦": "日羲",
  "明": "日月",
  "晚": "日免",
  "映": "日央",
  "暗": "日音",
  "曝": "日暴",
  "晰": "日析",
  "晓": "日尧",
  "晦": "日每",
  "昨": "日乍",
  "暇": "日叚",
  "晌": "日向",
  "曙": "日署",
  "晒": "日西",
  "昧": "日未",
  "旷": "日广",
  "晖": "日军",
  "晴": "日青",
  "蛾": "虫我",
  "虾": "虫下",
  "蠕": "虫需",
  "蝶": "虫枼",
  "蜂": "虫夆",
  "虹": "虫工",
  "蛇": "虫它",
  "蚊": "虫文",
  "蜡": "虫昔",
  "蛤": "虫合",
  "蟆": "虫莫",
  "螺": "虫累",
  "蜗": "虫呙",
  "蚂": "虫马",
  "蚁": "虫义",
  "影": "景彡",
  "题": "是页",
  "川": "丿〢",
  "顺": "川页",
  "别": "另刂",
  "鄙": "啚阝",
  "踉": "良",
  "跄": "仓",
  "蹭": "曾",
  "踩": "采",
  "踹": "耑",
  "踏": "沓",
  "躁": "喿",
  "跳": "兆",
  "路": "各",
  "踢": "易",
  "距": "巨",
  "蹑": "聂",
  "踊": "甬",
  "跨": "夸",
  "趺": "夫",
  "跃": "夭",
  "践": "戋",
  "趾": "止",
  "跺": "朵",
  "踪": "宗",
  "跑": "包",
  "跌": "失",
  "跟": "艮",
  "趴": "八",
  "蹁": "扁",
  "蹈": "舀",
  "蹬": "登",
  "跪": "危",
  "踱": "度",
  "跷": "尧",
  "蹲": "尊",
  "蹂": "柔",
  "躏": "蔺",
  "呀": "口牙",
  "呢": "口尼",
  "哈": "口合",
  "啊": "口阿",
  "叫": "口丩",
  "哪": "口那",
  "唉": "口矣",
  "哇": "口圭",
  "听": "口斤",
  "吧": "口巴",
  "吗": "口马",
  "哦": "口我",
  "吃": "口乞",
  "噪": "口喿",
  "喇": "口剌",
  "叭": "口八",
  "呼": "口乎",
  "吸": "口及",
  "啃": "口肯",
  "嘱": "口属",
  "唬": "口虎",
  "吓": "口下",
  "咳": "口亥",
  "卟": "口卜",
  "味": "口未",
  "叶": "口十",
  "唱": "口昌",
  "吻": "口勿",
  "嗷": "口敖",
  "啥": "口舍",
  "叹": "口又",
  "咱": "口自",
  "呓": "口艺",
  "嘴": "口觜",
  "喷": "口贲",
  "吵": "口少",
  "噜": "口鲁",
  "喻": "口俞",
  "喀": "口客",
  "咏": "口永",
  "啦": "口拉",
  "哋": "口地",
  "唔": "口吾",
  "嘿": "口黑",
  "呗": "口贝",
  "嘘": "口虚",
  "哧": "口赤",
  "吐": "口土",
  "喝": "口曷",
  "咬": "口交",
  "哄": "口共",
  "哼": "口亨",
  "叽": "口几",
  "嘛": "口麻",
  "啤": "口卑",
  "呛": "口仓",
  "呻": "口申",
  "吟": "口今",
  "喂": "口畏",
  "嘟": "口都",
  "哽": "口更",
  "喃": "口南",
  "嗨": "口海",
  "噻": "口塞",
  "咖": "口加",
  "啡": "口非",
  "哆": "口多",
  "嗦": "口索",
  "咆": "口包",
  "哮": "口孝",
  "吼": "口孔",
  "喊": "口咸",
  "呲": "口此",
  "哎": "口艾",
  "嘈": "口曹",
  "嘶": "口斯",
  "哑": "口亚",
  "喘": "口耑",
  "咧": "口列",
  "咿": "口伊",
  "噎": "口壹",
  "嚯": "口霍",
  "咐": "口付",
  "咦": "口夷",
  "唧": "口即",
  "哨": "口肖",
  "吱": "口支",
  "啼": "口帝",
  "嘀": "口商",
  "嗝": "口鬲",
  "吮": "口允",
  "呜": "口乌",
  "嘤": "口婴",
  "咕": "口古",
  "咂": "口匝",
  "咔": "口卡",
  "嚓": "口察",
  "嘎": "口戛",
  "咯": "口各",
  "嗯": "口恩",
  "吹": "口欠",
  "咋": "口乍",
  "咀": "口且",
  "嚼": "口爵",
  "嗲": "口爹",
  "咚": "口冬",
  "嗡": "口翁",
  "吭": "口亢",
  "哗": "口华",
  "嘻": "口喜",
  "噼": "口辟",
  "哩": "口里",
  "啪": "口拍",
  "唏": "口希",
  "喧": "口宣",
  "囔": "口囊",
  "噢": "口奥",
  "喔": "口屋",
  "叨": "口刀",
  "唯": "口隹",
  "咽": "口因",
  "喉": "口侯",
  "喽": "口娄",
  "嗓": "口桑",
  "嘹": "口尞",
  "叮": "口丁",
  "喁": "口禺",
  "噙": "口禽",
  "呵": "口可",
  "嗅": "口臭",
  "吆": "口幺",
  "呕": "口区",
  "哐": "口匡",
  "咙": "口龙",
  "嚷": "口襄",
  "唠": "口劳",
  "鸭": "甲鸟",
  "转": "车专",
  "辑": "车咠",
  "斩": "车斤",
  "加": "力口",
  "较": "车交",
  "轮": "车仑",
  "辆": "车两",
  "辖": "车害",
  "轨": "车九",
  "辐": "车畐",
  "轿": "车乔",
  "软": "车欠",
  "辎": "车甾",
  "辅": "车甫",
  "输": "车俞",
  "辗": "车展",
  "畔": "田半",
  "略": "田各",
  "畴": "田寿",
  "毗": "田比",
  "黠": "黑吉",
  "默": "黑犬",
  "黯": "黑音",
  "剁": "朵刂",
  "峰": "山夆",
  "岭": "山令",
  "岐": "山支",
  "鹦": "婴鸟",
  "购": "贝勾",
  "贱": "贝戋",
  "则": "贝刂",
  "败": "贝攵",
  "贼": "贝戎",
  "赠": "贝曾",
  "赋": "贝武",
  "赌": "贝者",
  "赐": "贝易",
  "贴": "贝占",
  "贩": "贝反",
  "财": "贝才",
  "赚": "贝兼",
  "删": "册刂",
  "邮": "由阝",
  "刚": "冈刂",
  "帆": "巾凡",
  "幅": "巾畐",
  "帜": "巾只",
  "帖": "巾占",
  "帐": "巾长",
  "帽": "巾冒",
  "雕": "周隹",
  "收": "丩攵",
  "剧": "居刂",
  "羽": "习习",
  "情": "忄青",
  "快": "忄夬",
  "性": "忄生",
  "懂": "忄董",
  "忆": "忄乙",
  "怙": "忄古",
  "悛": "忄夋",
  "恢": "忄灰",
  "慎": "忄真",
  "悼": "忄卓",
  "怪": "忄圣",
  "恰": "忄合",
  "恒": "忄亘",
  "怀": "忄不",
  "怜": "忄令",
  "怡": "忄台",
  "惕": "忄易",
  "慨": "忄既",
  "忙": "忄亡",
  "慌": "忄荒",
  "怔": "忄正",
  "惘": "忄罔",
  "憔": "忄焦",
  "悴": "忄卒",
  "恹": "忄厌",
  "懊": "忄奥",
  "悔": "忄每",
  "惯": "忄贯",
  "惶": "忄皇",
  "恍": "忄光",
  "惚": "忄忽",
  "愧": "忄鬼",
  "怅": "忄长",
  "愉": "忄俞",
  "怦": "忄平",
  "惭": "忄斩",
  "怯": "忄去",
  "悯": "忄闵",
  "憾": "忄感",
  "懒": "忄赖",
  "怖": "忄布",
  "懵": "忄瞢",
  "悻": "忄幸",
  "怕": "忄白",
  "惋": "忄宛",
  "惜": "忄昔",
  "忧": "忄尤",
  "憎": "忄曾",
  "惨": "忄参",
  "愤": "忄贲",
  "恨": "忄艮",
  "憧": "忄童",
  "憬": "忄景",
  "恸": "忄动",
  "忖": "忄寸",
  "惆": "忄周",
  "惊": "忄京",
  "慵": "忄庸",
  "慷": "忄康",
  "怆": "忄仓",
  "悦": "忄兑",
  "邺": "业阝",
  "数": "娄攵",
  "糕": "米羔",
  "籽": "米子",
  "粗": "米且",
  "精": "米青",
  "粘": "米占",
  "料": "米斗",
  "粉": "米分",
  "糨": "米强",
  "粮": "米良",
  "糖": "米唐",
  "糟": "米曹",
  "糊": "米胡",
  "粒": "米立",
  "烧": "火尧",
  "烁": "火乐",
  "燃": "火然",
  "烤": "火考",
  "烘": "火共",
  "煤": "火某",
  "灶": "火土",
  "炒": "火少",
  "烛": "火虫",
  "炽": "火只",
  "烟": "火因",
  "灿": "火山",
  "炮": "火包",
  "煌": "火皇",
  "灯": "火丁",
  "炉": "火户",
  "焰": "火臽",
  "烽": "火夆",
  "烦": "火页",
  "焊": "火旱",
  "炸": "火乍",
  "烂": "火兰",
  "烩": "火会",
  "炖": "火屯",
  "炫": "火玄",
  "熄": "火息",
  "爆": "火暴",
  "鹤": "隺鸟",
  "额": "客页",
  "豁": "害谷",
  "割": "害刂",
  "鲜": "鱼羊",
  "初": "衤刀",
  "被": "衤皮",
  "袍": "衤包",
  "补": "衤卜",
  "袖": "衤由",
  "裸": "衤果",
  "裤": "衤库",
  "衬": "衤寸",
  "衫": "衤彡",
  "袜": "衤末",
  "襟": "衤禁",
  "裙": "衤君",
  "褚": "衤者",
  "褪": "衤退",
  "裆": "衤当",
  "袄": "衤夭",
  "裕": "衤谷",
  "袂": "衤夬",
  "袱": "衤伏",
  "襦": "衤需",
  "禅": "礻单",
  "祥": "礻羊",
  "祸": "礻呙",
  "祛": "礻去",
  "礼": "礻乚",
  "视": "礻见",
  "祖": "礻且",
  "祝": "礻兄",
  "福": "礻畐",
  "社": "礻土",
  "祷": "礻寿",
  "神": "礻申",
  "祈": "礻斤",
  "褶": "礻習",
  "褂": "礻卦",
  "禳": "礻襄",
  "够": "句多",
  "触": "角虫",
  "皱": "刍皮",
  "邹": "刍阝",
  "雏": "刍隹",
  "孵": "卵孚",
  "鲍": "鱼包",
  "鲇": "鱼占",
  "刹": "杀刂",
  "外": "夕卜",
  "钱": "钅戋",
  "钢": "钅冈",
  "银": "钅艮",
  "针": "钅十",
  "销": "钅肖",
  "锭": "钅定",
  "锤": "钅垂",
  "镜": "钅竟",
  "铭": "钅名",
  "铠": "钅岂",
  "钮": "钅丑",
  "镶": "钅襄",
  "铺": "钅甫",
  "铃": "钅令",
  "铲": "钅产",
  "锅": "钅呙",
  "钥": "钅月",
  "锌": "钅辛",
  "锗": "钅者",
  "锂": "钅里",
  "钙": "钅丐",
  "锢": "钅固",
  "钟": "钅中",
  "钦": "钅欠",
  "铁": "钅失",
  "链": "钅连",
  "镇": "钅真",
  "钻": "钅占",
  "钧": "钅匀",
  "锦": "钅帛",
  "锋": "钅夆",
  "错": "钅昔",
  "铜": "钅同",
  "钛": "钅太",
  "钗": "钅叉",
  "钎": "钅千",
  "铛": "钅当",
  "铸": "钅寿",
  "锄": "钅助",
  "狡": "犭交",
  "猾": "犭骨",
  "猥": "犭畏",
  "猫": "犭苗",
  "狸": "犭里",
  "狗": "犭句",
  "猎": "犭昔",
  "猪": "犭者",
  "狠": "犭艮",
  "犹": "犭尤",
  "猜": "犭青",
  "猛": "犭孟",
  "狐": "犭瓜",
  "猴": "犭侯",
  "狭": "犭夹",
  "独": "犭虫",
  "狂": "犭王",
  "狼": "犭良",
  "狱": "犭讠犬",
  "饼": "饣并",
  "饿": "饣我",
  "饭": "饣反",
  "馈": "饣贵",
  "饱": "饣包",
  "饥": "饣几",
  "馒": "饣曼",
  "饶": "饣尧",
  "饯": "饣戋",
  "饮": "饣欠",
  "蚀": "饣虫",
  "的": "白勺",
  "翱": "皋羽",
  "欣": "斤欠",
  "所": "戶斤",
  "缺": "缶夬",
  "罐": "缶雚",
  "缸": "缶工",
  "掰": "手分手",
  "按": "扌安",
  "描": "扌苗",
  "挟": "扌夹",
  "抢": "扌仓",
  "抗": "扌亢",
  "擅": "扌亶",
  "扰": "扌尤",
  "扯": "扌止",
  "撕": "扌斯",
  "捎": "扌肖",
  "搏": "扌尃",
  "控": "扌空",
  "抓": "扌爪",
  "抄": "扌少",
  "捕": "扌甫",
  "抱": "扌包",
  "授": "扌受",
  "拦": "扌兰",
  "找": "扌戈",
  "捉": "扌足",
  "探": "扌罙",
  "打": "扌丁",
  "扫": "扌彐",
  "把": "扌巴",
  "拆": "扌斥",
  "折": "扌斤",
  "护": "扌户",
  "搞": "扌高",
  "技": "扌支",
  "接": "扌妾",
  "拼": "扌并",
  "持": "扌寺",
  "排": "扌非",
  "抵": "扌氐",
  "换": "扌奂",
  "投": "扌殳",
  "扣": "扌口",
  "批": "扌比",
  "据": "扌居",
  "提": "扌是",
  "推": "扌隹",
  "托": "扌乇",
  "搜": "扌叟",
  "拔": "扌犮",
  "操": "扌喿",
  "指": "扌旨",
  "拯": "扌丞",
  "捷": "扌疌",
  "损": "扌员",
  "招": "扌召",
  "括": "扌舌",
  "捺": "扌奈",
  "抬": "扌台",
  "撰": "扌巽",
  "拍": "扌白",
  "挪": "扌那",
  "播": "扌番",
  "拐": "扌另",
  "摆": "扌罢",
  "抽": "扌由",
  "扶": "扌夫",
  "拷": "扌考",
  "拉": "扌立",
  "摘": "扌啇",
  "握": "扌屋",
  "搭": "扌荅",
  "撇": "扌敝",
  "抛": "扌九力",
  "摄": "扌聂",
  "拟": "扌以",
  "拨": "扌发",
  "掀": "扌欣",
  "拓": "扌石",
  "揽": "扌览",
  "抹": "扌末",
  "插": "扌臿",
  "撼": "扌感",
  "挂": "扌圭",
  "擦": "扌察",
  "扎": "扌乚",
  "扮": "扌分",
  "措": "扌昔",
  "担": "扌旦",
  "揭": "扌曷",
  "撞": "扌童",
  "掉": "扌卓",
  "抑": "扌卬",
  "抿": "扌民",
  "摊": "扌难",
  "摸": "扌莫",
  "振": "扌辰",
  "挺": "扌廷",
  "掘": "扌屈",
  "扔": "扌乃",
  "捧": "扌奉",
  "拎": "扌令",
  "撒": "扌散",
  "拘": "扌句",
  "抚": "扌无",
  "掐": "扌臽",
  "搁": "扌阁",
  "搐": "扌畜",
  "攥": "扌纂",
  "搓": "扌差",
  "揍": "扌奏",
  "挤": "扌齐",
  "抖": "扌斗",
  "捂": "扌吾",
  "披": "扌皮",
  "搬": "扌般",
  "捏": "扌圼",
  "掏": "扌匋",
  "捡": "扌佥",
  "扭": "扌丑",
  "拱": "扌共",
  "搅": "扌觉",
  "拌": "扌半",
  "挫": "扌坐",
  "掠": "扌京",
  "挨": "扌矣",
  "拭": "扌式",
  "揉": "扌柔",
  "扒": "扌八",
  "拧": "扌宁",
  "撅": "扌厥",
  "捣": "扌岛",
  "搂": "扌娄",
  "拾": "扌合",
  "捐": "扌肙",
  "揣": "扌耑",
  "攆": "扌輦",
  "撵": "扌辇",
  "拂": "扌弗",
  "摁": "扌恩",
  "撮": "扌最",
  "撩": "扌尞",
  "拢": "扌龙",
  "拽": "扌曳",
  "拗": "扌幼",
  "挠": "扌尧",
  "捅": "扌甬",
  "攒": "扌赞",
  "拴": "扌全",
  "扑": "扌卜",
  "押": "扌甲",
  "携": "扌隽",
  "执": "扌丸",
  "扩": "扌广",
  "挣": "扌争",
  "拒": "扌巨",
  "撑": "扌掌",
  "挥": "扌军",
  "掩": "扌奄",
  "挡": "扌当",
  "抒": "扌予",
  "搔": "扌蚤",
  "挑": "扌兆",
  "揪": "扌秋",
  "拙": "扌出",
  "摒": "扌屏",
  "挞": "扌达",
  "掷": "扌郑",
  "捶": "扌垂",
  "撂": "扌畧",
  "歌": "哥欠",
  "飘": "票风",
  "瓢": "票瓜",
  "酷": "酉告",
  "酸": "酉夋",
  "醉": "酉卒",
  "酵": "酉孝",
  "酥": "酉禾",
  "醋": "酉昔",
  "酗": "酉凶",
  "酩": "酉名",
  "酊": "酉丁",
  "醺": "酉熏",
  "酬": "酉州",
  "配": "酉己",
  "醒": "酉星",
  "醇": "酉享",
  "顶": "丁页",
  "柄": "木丙",
  "林": "木木",
  "柱": "木主",
  "杨": "木昜",
  "样": "木羊",
  "标": "木示",
  "樱": "木婴",
  "桃": "木兆",
  "构": "木勾",
  "杭": "木亢",
  "柿": "木市",
  "机": "木几",
  "析": "木斤",
  "核": "木亥",
  "棋": "木其",
  "相": "木目",
  "棍": "木昆",
  "板": "木反",
  "校": "木交",
  "模": "木莫",
  "检": "木佥",
  "栈": "木戋",
  "枝": "木支",
  "栏": "木兰",
  "框": "木匡",
  "横": "木黄",
  "概": "木既",
  "梯": "木弟",
  "楷": "木皆",
  "桂": "木圭",
  "棒": "木奉",
  "材": "木才",
  "棚": "木朋",
  "椅": "木奇",
  "杯": "木不",
  "档": "木当",
  "枫": "木风",
  "杜": "木土",
  "枕": "木冘",
  "梭": "木夋",
  "柏": "木白",
  "桶": "木甬",
  "朴": "木卜",
  "枰": "木平",
  "楸": "木秋",
  "枉": "木王",
  "桩": "木庄",
  "械": "木戒",
  "柜": "木巨",
  "槽": "木曹",
  "杆": "木干",
  "橱": "木厨",
  "株": "木朱",
  "栩": "木羽",
  "柳": "木卯",
  "橡": "木象",
  "椭": "木陏",
  "棉": "木帛",
  "梢": "木肖",
  "村": "木寸",
  "根": "木艮",
  "楼": "木娄",
  "树": "木对",
  "桥": "木乔",
  "极": "木及",
  "梅": "木每",
  "枪": "木仓",
  "格": "木各",
  "檐": "木詹",
  "权": "木又",
  "松": "木公",
  "枯": "木古",
  "槁": "木高",
  "植": "木直",
  "鹅": "我鸟",
  "翻": "番羽",
  "射": "身寸",
  "躺": "身尚",
  "躲": "身朵",
  "躯": "身区",
  "稻": "禾舀",
  "利": "禾刂",
  "私": "禾厶",
  "种": "禾中",
  "程": "禾呈",
  "移": "禾多",
  "租": "禾且",
  "和": "禾口",
  "称": "禾尔",
  "科": "禾斗",
  "税": "禾兑",
  "秋": "禾火",
  "秸": "禾吉",
  "秆": "禾干",
  "稿": "禾高",
  "稀": "禾希",
  "秒": "禾少",
  "稼": "禾家",
  "秽": "禾岁",
  "稳": "禾急",
  "秘": "禾必",
  "稍": "禾肖",
  "秣": "禾末",
  "穰": "禾襄",
  "积": "禾只",
  "稚": "禾隹",
  "徒": "彳走",
  "彼": "彳皮",
  "徘": "彳非",
  "徊": "彳回",
  "行": "彳亍",
  "律": "彳聿",
  "待": "彳寺",
  "很": "彳艮",
  "循": "彳盾",
  "御": "彳卸",
  "衍": "彳氵亍",
  "街": "彳圭亍",
  "衔": "彳钅亍",
  "彻": "彳切",
  "徐": "彳余",
  "征": "彳正",
  "往": "彳主",
  "物": "牜勿",
  "特": "牜寺",
  "牺": "牜西",
  "牲": "牜生",
  "牧": "牜攵",
  "犊": "牛卖",
  "知": "矢口",
  "矩": "矢巨",
  "矮": "矢委",
  "敏": "每攵",
  "舰": "舟见",
  "般": "舟殳",
  "航": "舟亢",
  "鹄": "告鸟",
  "剩": "乘刂",
  "敌": "舌攵",
  "乱": "舌乚",
  "辞": "舌辛",
  "甜": "舌甘",
  "鼾": "鼻干",
  "牍": "片卖",
  "版": "片反",
  "牌": "片卑",
  "牒": "片枼",
  "新": "亲斤",
  "瓶": "并瓦",
  "剃": "弟刂",
  "站": "立占",
  "靖": "立青",
  "竣": "立夋",
  "端": "立耑",
  "颜": "彦页",
  "部": "咅阝",
  "剖": "咅刂",
  "韵": "音匀",
  "郑": "关阝",
  "效": "交攵",
  "歉": "兼欠",
  "翔": "羽",
  "壮": "丬士",
  "妆": "丬女",
  "将": "丬寽",
  "状": "丬犬",
  "况": "冫兄",
  "次": "冫欠",
  "减": "冫咸",
  "凝": "冫疑",
  "凛": "冫禀",
  "冯": "冫马",
  "决": "冫夬",
  "凑": "冫奏",
  "凄": "冫妻",
  "准": "冫隹",
  "冲": "冫中",
  "冰": "冫水",
  "凉": "冫京",
  "凌": "冫夌",
  "冷": "冫令",
  "净": "冫争",
  "邵": "召阝",
  "郡": "君阝",
  "群": "君羊",
  "剥": "录刂",
  "鸠": "九鸟",
  "骗": "马扁",
  "劝": "又力",
  "妖": "女夭",
  "奴": "女又",
  "婵": "女单",
  "娜": "女那",
  "好": "女子",
  "姚": "女兆",
  "如": "女口",
  "娃": "女圭",
  "她": "女也",
  "姓": "女生",
  "奸": "女干",
  "始": "女台",
  "嫌": "女兼",
  "婚": "女昏",
  "娱": "女吴",
  "媒": "女某",
  "姐": "女且",
  "姗": "女册",
  "妇": "女彐",
  "嫩": "女敕",
  "娆": "女尧",
  "嫉": "女疾",
  "妒": "女户",
  "妈": "女马",
  "嫁": "女家",
  "娇": "女乔",
  "嫖": "女票",
  "姑": "女古",
  "妩": "女无",
  "媚": "女眉",
  "婿": "女胥",
  "妹": "女未",
  "姣": "女交",
  "奶": "女乃",
  "姆": "女母",
  "姥": "女老",
  "妃": "女己",
  "妞": "女丑",
  "姻": "女因",
  "嫂": "女叟",
  "娴": "女闲",
  "姨": "女夷",
  "婉": "女宛",
  "媳": "女息",
  "嬉": "女喜",
  "妙": "女少",
  "娘": "女良",
  "妓": "女支",
  "舒": "舍予",
  "领": "令页",
  "颔": "含页",
  "邻": "令阝",
  "剑": "佥刂",
  "叙": "余又",
  "斜": "余斗",
  "创": "仓刂",
  "敛": "佥攵",
  "颂": "公页",
  "欲": "谷欠",
  "伟": "亻韦",
  "储": "亻诸",
  "你": "亻尔",
  "他": "亻也",
  "偏": "亻扁",
  "信": "亻言",
  "何": "亻可",
  "但": "亻旦",
  "件": "亻牛",
  "保": "亻呆",
  "像": "亻象",
  "做": "亻故",
  "什": "亻十",
  "位": "亻立",
  "住": "亻主",
  "停": "亻亭",
  "供": "亻共",
  "代": "亻弋",
  "们": "亻门",
  "优": "亻尤",
  "值": "亻直",
  "传": "亻专",
  "作": "亻乍",
  "任": "亻壬",
  "使": "亻吏",
  "倚": "亻奇",
  "化": "亻匕",
  "仅": "亻又",
  "仿": "亻方",
  "偃": "亻匽",
  "例": "亻列",
  "俗": "亻谷",
  "价": "亻介",
  "俄": "亻我",
  "亿": "亻乙",
  "伙": "亻火",
  "伴": "亻半",
  "佼": "亻交",
  "催": "亻崔",
  "健": "亻建",
  "俊": "亻夋",
  "傲": "亻敖",
  "佬": "亻老",
  "侦": "亻贞",
  "佑": "亻右",
  "佛": "亻弗",
  "侮": "亻每",
  "份": "亻分",
  "仕": "亻士",
  "倡": "亻昌",
  "仲": "亻中",
  "仔": "亻子",
  "倍": "亻咅",
  "仪": "亻义",
  "伯": "亻白",
  "伦": "亻仑",
  "偷": "亻俞",
  "傅": "亻尃",
  "伸": "亻申",
  "似": "亻以",
  "付": "亻寸",
  "估": "亻古",
  "倜": "亻周",
  "傥": "亻党",
  "债": "亻责",
  "侣": "亻吕",
  "仙": "亻山",
  "俯": "亻府",
  "俩": "亻两",
  "俱": "亻具",
  "俺": "亻奄",
  "仨": "亻三",
  "僻": "亻辟",
  "俨": "亻严",
  "偎": "亻畏",
  "伶": "亻令",
  "俐": "亻利",
  "侥": "亻尧",
  "偌": "亻若",
  "借": "亻昔",
  "仰": "亻卬",
  "仗": "亻丈",
  "休": "亻木",
  "俘": "亻孚",
  "伍": "亻五",
  "倒": "亻到",
  "便": "亻更",
  "仁": "亻二",
  "依": "亻衣",
  "伐": "亻戈",
  "侧": "亻则",
  "低": "亻氐",
  "体": "亻本",
  "仍": "亻乃",
  "侍": "亻寺",
  "促": "亻足",
  "仇": "亻九",
  "儒": "亻需",
  "佐": "亻左",
  "伪": "亻为",
  "侩": "亻会",
  "假": "亻叚",
  "佳": "亻圭",
  "伏": "亻犬",
  "偶": "亻禺",
  "偿": "亻尝",
  "倦": "亻卷",
  "张": "弓长",
  "强": "弓虽",
  "弹": "弓单",
  "引": "弓丨",
  "弛": "弓也",
  "弧": "弓瓜",
  "弦": "弓玄",
  "弥": "弓尔",
  "弘": "弓厶",
  "比": "匕匕",
  "幼": "幺力",
  "绰": "纟卓",
  "纵": "纟从",
  "纷": "纟分",
  "纤": "纟千",
  "缚": "纟尃",
  "绷": "纟朋",
  "纫": "纟刃",
  "绢": "纟肙",
  "组": "纟且",
  "给": "纟合",
  "红": "纟工",
  "纸": "纟氏",
  "结": "纟吉",
  "纪": "纟己",
  "编": "纟扁",
  "线": "纟戋",
  "统": "纟充",
  "级": "纟及",
  "络": "纟各",
  "续": "纟卖",
  "绞": "纟交",
  "终": "纟冬",
  "绝": "纟色",
  "绘": "纟会",
  "纯": "纟屯",
  "绵": "纟帛",
  "综": "纟宗",
  "纠": "纟丩",
  "绕": "纟尧",
  "缕": "纟娄",
  "绪": "纟者",
  "绩": "纟责",
  "织": "纟只",
  "纱": "纟少",
  "绿": "纟录",
  "绽": "纟定",
  "缩": "纟宿",
  "纨": "纟丸",
  "绔": "纟夸",
  "缀": "纟叕",
  "缰": "纟畺",
  "缝": "纟逢",
  "绳": "纟黾",
  "绊": "纟半",
  "绯": "纟非",
  "缄": "纟咸",
  "缆": "纟览",
  "缴": "纟敫",
  "绅": "纟申",
  "纳": "纟内",
  "约": "纟勺",
  "绍": "纟召",
  "绶": "纟受",
  "纶": "纟仑",
  "细": "纟田",
  "缢": "纟益",
  "维": "纟隹",
  "敲": "高攴",
  "就": "京尤",
  "敦": "享攵",
  "刘": "文刂",
  "斓": "文阑",
  "放": "方攵",
  "颤": "亶页",
  "氓": "亡民",
  "剂": "齐刂",
  "刻": "亥刂",
  "郭": "享阝",
  "鹧": "庶鸟",
  "麟": "鹿粦",
  "郊": "交阝",
  "谈": "讠炎",
  "谁": "讠隹",
  "说": "讠兑",
  "话": "讠舌",
  "许": "讠午",
  "该": "讠亥",
  "调": "讠周",
  "试": "讠式",
  "记": "讠己",
  "设": "讠殳",
  "语": "讠吾",
  "让": "讠上",
  "请": "讠青",
  "认": "讠人",
  "讲": "讠井",
  "识": "讠只",
  "谋": "讠某",
  "详": "讠羊",
  "诸": "讠者",
  "证": "讠正",
  "访": "讠方",
  "读": "讠卖",
  "词": "讠司",
  "诗": "讠寺",
  "谜": "讠迷",
  "诠": "讠全",
  "课": "讠果",
  "订": "讠丁",
  "谐": "讠皆",
  "谨": "讠堇",
  "讹": "讠化",
  "训": "讠川",
  "诀": "讠夬",
  "谍": "讠枼",
  "诅": "讠且",
  "谎": "讠荒",
  "谬": "讠翏",
  "谢": "讠射",
  "讼": "讠公",
  "谱": "讠普",
  "谊": "讠宜",
  "诵": "讠甬",
  "诧": "讠宅",
  "谯": "讠焦",
  "诞": "讠延",
  "讨": "讠寸",
  "诚": "讠成",
  "讧": "讠工",
  "评": "讠平",
  "诏": "讠召",
  "谓": "讠胃",
  "误": "讠吴",
  "讯": "讠卂",
  "论": "讠仑",
  "议": "讠义",
  "计": "讠十",
  "谦": "讠兼",
  "谅": "讠京",
  "询": "讠旬",
  "诈": "讠乍",
  "诉": "讠斥",
  "诱": "讠秀",
  "讶": "讠牙",
  "讷": "讠内",
  "讽": "讠风",
  "诫": "讠戒",
  "诺": "讠若",
  "诋": "讠氐",
  "谴": "讠遣",
  "限": "阝艮",
  "帕": "巾白",
  "伊": "亻尹",
  "掖": "扌夜",
  "列": "歹刂",
  "呃": "口厄",
  "颁": "分页",
  "纽": "纟丑",
  "瑚": "王胡",
  "键": "钅建",
  "捆": "扌困",
  "绑": "纟邦",
  "剽": "票刂",
  "蹦": "崩",
  "猖": "犭昌",
  "獗": "犭厥",
  "栋": "木东",
  "悚": "忄束",
  "幌": "巾晃",
  "赔": "贝咅",
  "吁": "口于",
  "锐": "钅兑",
  "哟": "口约",
  "剔": "易刂",
  "朽": "木丂",
  "吖": "口丫",
  "儆": "亻敬",
  "锈": "钅秀",
  "附": "阝付",
  "滔": "氵舀",
  "婊": "女表",
  "坊": "土方",
  "彰": "章彡",
  "懈": "忄解",
  "湛": "氵甚",
  "粥": "弓米弓",
  "妨": "女方",
  "胁": "月办",
  "腿": "月退",
  "邓": "又阝",
  "嗖": "口叟",
  "璐": "王路",
  "喵": "口苗",
  "槛": "木监",
  "朝": "龺月",
  "韩": "龺韦"
}

#开始时间
time1 = time.time()
#特殊符号集合
SpecialCode=['`','1','2','3','4','5','6','7','8','9','0','-','=','[',']','\\','\'',';',',',
             '.','/','~','!','@','#','$','%','^','&','*','(',')','_','+','{','}','|',':','"',
             '<','>','?','…','·','*','【','】','？','《','》','：','“','，','。','、','/',' ','￥','！']
#创建空字典，将‘错误文本：正确文本’以键值对的形式存于该字典中
dict = {}
#检测出的敏感词总数，初始化为0
total = 0

class DfaFilter(object):
    def __init__(self):
        super(DfaFilter, self).__init__()
        #创建一个空敏感字字典
        self.Sensitive_dict={}
        #定义结束标志
        self.delimit = '\x00'

    #将敏感词导入并进行预处理
    def GetSensitiveWords(self, path):
        #打开敏感词文本，因为python的默认编码方式是gbk，而windows是utf-8，所以这里要用utf-8，否则打不开
        WordsHandler = open (path, encoding='utf-8')
        while True:
            #按行读取敏感词并去除读取字符串尾的换行符
            keywords = WordsHandler.readline().rstrip('\n')
            #针对拆分偏旁建树
            ppform = ''
            for i in keywords:
                #过滤字母
                if i not in zimubiao:
                    if i in chazi:
                      #将敏感字在拆分偏旁字典中查询拆分后的部分
                      ppform += ''.join(chazi[i])
                     else:
                      ppform += ''.join(i)
            #将其形成键值对放入字典
            dict[ppform] = keywords
            #将其送入敏感词树建立函数
            self.AddSensitiveWords(ppform)
            #这里创建一个空列表，用来装一个字的拼音及其首字母
            pylist=[]
            #将一个敏感词的每一个敏感字都转成拼音及其首字母的形式
            for i in keywords:
                pyform = ""
                Firstcode = ""
                for index, value in enumerate(pypinyin.pinyin(i, style=pypinyin.NORMAL)):
                    #用join函数将转化成的拼音变成字符串
                    pyform += "".join(value)
                    #首字母
                    Firstcode += "".join(value[0][0])
                    pylist.append([pyform, Firstcode])
            self.DiGui(pylist, 0, len(keywords), '', keywords)
            #读入的关键词为空，则break
            if not keywords:
                break
        WordsHandler.close()

    #递归函数，将每个字的拼音或首字母与其他字的拼音和首字母进行排列组合，比如傻子:shaz or shazi
    def DiGui(self, pylist, i, length, chars, keywords):
        if i == length:
            #错误文本：正确文本
            dict[chars] = keywords
            #将排列组合后的敏感词字母送入敏感词生成树函数
            self.AddSensitiveWords(chars)
            return
        #将chars与下一个字的拼音合并
        self.DiGui(pylist, i+1, length, chars + pylist[i][0], keywords)
        #将chars与下一个字的首字母合并
        self.DiGui(pylist, i+1, length, chars + pylist[i][1], keywords)
        return


    def AddSensitiveWords(self, stword):
        if not stword:
            return
        #定义一个字典tree
        tree = self.Sensitive_dict
        for i in range(len(stword)):
            #如果这个字母已经在字典中，则字典跳转到该字母的下一个结点
            if stword[i] in tree:
                tree = tree[stword[i]]
            #如果不在就创建一个新结点
            else:
                for j in range(i, len(stword)):
                    #新结点首先为空
                    tree[stword[j]] = {}
                    #得到新树和新结点
                    last_tree = tree
                    last_char = stword[j]
                    #跳转到新结点的位置
                    tree = tree[stword[j]]
                #全部导入之后，打上结束键值对
                last_tree[last_char] = {self.delimit: 0}
                break
            if i == len(stword) - 1:
                tree[self.delimit] = 0


    def FilterSensitiveWords(self, message, linepos, ret):
        #起始位置
        start = 0
        #一行的敏感词总数
        part_total = 0
        while start < len(message):
            tree = self.Sensitive_dict
            #将文本进行切片后检测，比如start不断++，直到检测到敏感词头，则过滤后，start到达敏感词尾，然后继续切片检测
            message_chars = message[start:]
            #正常状态下，放入敏感词字母
            normal_ret = ''
            #分支状态下，放入敏感词字母，为了回退的时候，加入的字母也能同时回退，直接设置两个空字符串
            mirror_image_ret = ''
            #正常步数
            normal_step = 0
            #回退步数
            mirror_image_step = 0
            stop = 0
            #已经检测到敏感词标志
            Code_flag = 0
            #进入分支状态标志
            Branch_flag = 0
            for char in message_chars:
                #创建一个空字符串，用来存待检测字的拼音
                pychar=''
                for index,value in enumerate(pypinyin.pinyin(char,style=pypinyin.NORMAL)):
                    pychar+=''.join(value).lower()
                #front为敏感词头在原文本中的位置
                front = start
                #Code_flag状态为1，表明正在检测一个敏感词，此时如果待检测的字为特殊符号，则步数+1，进入下一次循环
                if Code_flag == 1 and pychar[0] in SpecialCode:
                    #检测的位置不能超过待检测文本长度
                    if (start+normal_step+1) < len(message):
                        #该记号表明前面遇到了分支,镜像步数用于回退
                        if Branch_flag == 1:
                            normal_step += 1
                            mirror_image_step += 1
                            continue
                        #若未遇到分支，则正常步数+1
                        else:
                            normal_step += 1
                            continue

                #遍历字符串中的每个字母
                for i in pychar:
                    #如果这个字母在敏感词树中
                    if i in tree:
                        #对于正常状态下，且值不含结束键的字母存入normal_ret
                        if Branch_flag == 0 and self.delimit not in tree[i]:
                            normal_ret += ''.join(i)
                        #对于值只有结束键的字母
                        elif self.delimit in tree[i] and len(tree[i]) == 1:
                            #分支状态
                            if Branch_flag == 1:
                                mirror_image_ret += ''.join(i)
                            #正常状态
                            else:
                                normal_ret += ''.join(i)
                        #分支状态下或者值不仅仅包含结束键
                        else:
                            #区分此时的字母在原文本中是为单字母还是一个字的拼音的一个字母
                            #如果是一个字的拼音的一个字母，比如falungong中的前一个g
                            if len(pychar) != 1:
                                mirror_image_ret += ''.join(i)
                            #如果是单字母，比如falg中的g
                            else:
                                normal_ret += ''.join(i)
                        Code_flag = 1
                        #结束键不在这个字母的字典中
                        if self.delimit not in tree[i]:
                            #跳转到i结点
                            tree = tree[i]
                        #结束键在这个字母的字典中，但子树的字典键值对不止一个，表明此时遇到了分支，进入分支状态
                        elif self.delimit in tree[i] and len(tree[i]) != 1:
                            Branch_flag = 1
                            #跳转到i结点
                            tree = tree[i]
                        #这个字母的字典里只有结束键,表示找到了敏感词尾
                        else:
                            #找到敏感词尾的位置
                            start += normal_step
                            back = start
                            part_total += 1
                            #找到错误文本对应的正确文本
                            true = dict[normal_ret+mirror_image_ret]
                            # 将结果写入ret列表中
                            ret.append('Line'+str(linepos)+':'+'<'+true+'>'+message[front:back+1])
                            #停止遍历
                            stop = 1
                            break
                    #如果这个字母不在敏感词树中
                    else:
                        #如果为分支状态
                        if Branch_flag == 1:
                            if normal_ret in dict:
                                start += normal_step
                                #步数回退
                                start -= mirror_image_step
                                back = start
                                part_total += 1
                                true = dict[normal_ret]
                                ret.append('line' + str(linepos) + ':' + '<' + true + '>' + message[front:back+1])
                                #重置分支状态
                                Branch_flag = 0
                                #停止遍历
                                stop = 1
                                break
                            else:
                                start += normal_step
                                start -= mirror_image_step
                                stop = 1
                                break
                        else:
                            #停止遍历
                            stop = 1
                            break
                if stop == 1:
                    break
                #分支状态下，镜像步数和正常步数要同步，用于回退
                if Branch_flag == 1:
                    normal_step += 1
                    mirror_image_step += 1
                else:
                    normal_step += 1
            start += 1
        #返回敏感词数量
        return part_total,ret

    #针对拆分偏旁进行过滤
    def SplitSideFilter(self,message,linepos,ret):
        start = 0
        part_total = 0
        message = message.lower()
        while start < len(message):
            tree = self.Sensitive_dict
            step = 0
            Ret = ''
            front = start
            message_chars = message[start:]
            for char in message_chars:
                #因为拆分偏旁一定是汉字，所以排除字母
                if char in tree and char not in zimubiao:
                    Ret += ''.join(char)
                    step += 1
                    if self.delimit not in tree[char]:
                        tree = tree[char]
                    else:
                        start += step - 1
                        back = start
                        part_total += 1
                        true = dict[Ret]
                        ret.append('Line' + str(linepos) + ':' + '<' + true + '>' + message[front:back + 1])
                else:
                    break
            start += 1
        return part_total,ret

if __name__ == "__main__":
    #实例化对象
    x = DfaFilter()
    x.GetSensitiveWords('words.txt')
    #在python中默认的编码方式是 “ gbk ”，而Windows中的文件默认的编码方式是 “ utf-8 ”
    OrgHandler = open('org.txt', encoding='utf-8')
    linepos = 1
    empty_flag = 0
    # 一个空列表，用来暂时储存过滤结果
    ret = []
    while True:
        # 获取文件的每行内容
        line = OrgHandler.readline().rstrip('\n')
        #整个文本的敏感词总数
        result,ret=x.FilterSensitiveWords(line, linepos, ret)
        total += result
        result,ret= x.SplitSideFilter(line, linepos, ret)
        total +=result
        #行数++
        linepos += 1
        if not line:
            flag1+=1
        if line:
            flag1 = 0
        #当空行数量大于3时才跳出
        if flag1 > 3:
            break
    OrgHandler.close()
    #将列表里的结果按顺序打印在输出文本中
    ret.append(str(total))
    file = open("D:/pythonProject/031902213/ans.txt", 'w')
    y=len(ret)-1
    file.write('total:')
    file.write(str(ret[y]))
    file.write('\n')
    for i in range(len(ret)-1):
        file.write(str(ret[i]))
        file.write('\n')
    time2 = time.time()
    print('总共耗时:' + str(time2 - time1) + 's')
    print(u'当前进程的内存使用：%.4f GB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 / 1024) )

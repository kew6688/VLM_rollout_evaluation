# Metric计算方式

|CLASS|TASK|SCORE（前面是权重）|SUPPLEMENT|DESCPRITION|atomic\_skill|
|---|---|---|---|---|---|
|**Pick and Place**|apple\_from\_shelf|- \(1/1\) 苹果位置超出栏杆算成功拿出|||\[<br>\[<br>\[<br>\["Move", "Grasp"\]<br>\]<br>\]<br>\]|
||apple\_to\_fruit\_bowl|- \(1/1\) 苹果放入碗中|||\[<br>\[<br>\[<br>\["Move", "Grasp", "Place"\]<br>\]<br>\]<br>\]|
||bookmark\_on\_book|- \(1/1\) 书签放置书上（至少40%重叠）|||\[<br>\[<br>\[<br>\["Move", "Grasp", "Place"\]<br>\]<br>\]<br>\]|
||bowl\_to\_plate|- \(1/1\) 三个碗任意一个夹至盘子上|||\[<br>\[<br>\[<br>\["Move", "Grasp", "Place"\]<br>\],<br>\[<br>\["Move", "Grasp", "Place"\]<br>\],<br>\[<br>\["Move", "Grasp", "Place"\]<br>\]<br>\]<br>\]|
||perfume\_to\_cosmetics\_rack|- \(0\.5/1\) 香水瓶放到盒子上方<br>- \(0\.5/1\) 香水瓶插进盒子其中的格子里 |||\[<br>\[<br>\[<br>\["Move", "Grasp"\]<br>\]<br>\],<br>\[<br>\[<br>\["Insert"\]<br>\]<br>\]<br>\]|
||remote\_to\_holder|- \(1/1\) 遥控器放置盒子上（至少40%重叠）|||\[<br>\[<br>\[<br>\["Move", "Grasp", "Place"\]<br>\]<br>\]<br>\]|
||salt\_to\_spice\_rack|- \(1/1\) 调料瓶放到架子里|||\[<br>\[<br>\[<br>\["Move", "Grasp", "Place"\]<br>\]<br>\]<br>\]|
||soap\_to\_dish|- \(1/1\) 肥皂放到盒子上|||\[<br>\[<br>\[<br>\["Move", "Grasp", "Place"\]<br>\]<br>\]<br>\]|
||teacup\_to\_saucer\_teapot\_to\_tray|- \(0\.5/1\) 茶杯放到碟子上<br>- \(0\.5/1\) 茶壶放到盒子上 （不分先后）|||\[<br>\[<br>\[<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\]<br>\]<br>\]<br>\]|
||utensils\_to\_holder|- \(0\.5/1\) 勺子放到盒子上<br>- \(0\.5/1\) 叉子放到盒子上 （不分先后）|||\[<br>\[<br>\[<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\]<br>\]<br>\]<br>\]|
|**Long\-Horizon**|bottle|- 每个瓶子 1/12|||\[<br>\[<br>\[<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\]<br>\]<br>\]<br>\]|
||Detergent|- 每个洗涤剂 1/3|||\[<br>\[<br>\[<br>\["Grasp", "Place", "Handover"\],<br>\["Grasp", "Place", "Handover"\],<br>\["Grasp", "Place", "Handover"\]<br>\]<br>\]<br>\]|
||Dish|- 每个餐具、盘子1/5|||\[<br>\[<br>\[<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\]<br>\]<br>\]<br>\]|
||Dishwasher|- 开 Dishwasher 1/2<br>- 两个碗放进去各自 1/6<br>- 关闭 1/6|||\[<br>\[<br>\[<br>\["Move", "Pull", "Sweep"\]<br>\]<br>\],<br>\[<br>\[<br>\["Move", "Push"\],<br>\["Move", "Grasp", "Place"\],<br>\["Move", "Grasp", "Place"\]<br>\]<br>\]<br>\]|
||Fruit|- 三个水果放进去各自 1/5<br>- 倒水 2/5|||\[<br>\[<br>\[<br>\["Grasp", "Place", "Handover"\],<br>\["Grasp", "Place", "Handover"\],<br>\["Grasp", "Place", "Handover"\],<br>\["Move", "Grasp", "Pour"\],<br>\["Move", "Grasp", "Pour"\]<br>\]<br>\]<br>\]|
||Make sandwich|- 每一片叠在前一片上面 1/4|||\[<br>\[<br>\[<br>\["Move", "Grasp", "Place", "Sweep"\],<br>\["Move", "Grasp", "Place", "Sweep"\],<br>\["Move", "Grasp", "Place", "Sweep"\],<br>\["Move", "Grasp", "Place", "Sweep"\]<br>\]<br>\]<br>\]|
||Microwave|- 开 Microwave 1/2<br>- 两个蛋挞放进去各自 1/6<br>- 关闭 Microwave 1/6|||\[<br>\[<br>\[<br>\["Pull", "Grasp", "Sweep"\]<br>\]<br>\],<br>\[<br>\[<br>\["Move", "Sweep"\],<br>\["Grasp", "Place"\],<br>\["Grasp", "Place"\]<br>\]<br>\]<br>\]|
||pen|- 三个笔各自 1/3|||\[<br>\[<br>\[<br>\["Grasp", "Insert"\],<br>\["Grasp", "Insert"\],<br>\["Grasp", "Insert"\]<br>\]<br>\]<br>\]|
||shop|- 六个物体在收银区域停留 30 step 各自 1/6<br>- 六个物体放置在左侧各自 1/6|||\[<br>\[<br>\[<br>\["Move", "Grasp", "Handover"\],<br>\["Move", "Grasp", "Handover"\],<br>\["Move", "Grasp", "Handover"\],<br>\["Move", "Grasp", "Handover"\],<br>\["Move", "Grasp", "Handover"\],<br>\["Move", "Grasp", "Handover"\],<br>\["Move", "Place"\],<br>\["Move", "Place"\],<br>\["Move", "Place"\],<br>\["Move", "Place"\],<br>\["Move", "Place"\],<br>\["Move", "Place"\]<br>\]<br>\]<br>\]|
|**Dexterous \& Precise **|collect\_coffee\_beans|- \(0\.5\) 盖子放在罐子上，中心轴相近，盖子平行于桌面<br>- \(0\.5 / 7\) 咖啡豆1在罐子里<br>- \(0\.5 / 7\) 咖啡豆2在罐子里<br>- \.\.\. \.\.\.<br>- \(0\.5 / 7\) 咖啡豆7在罐子里<br>||\[<br>\[<br>\[<br>盖子放在罐子上，中心轴相近，盖子平行于桌面,<br>咖啡豆1在罐子里,<br>咖啡豆2在罐子里,<br>咖啡豆3在罐子里,<br>咖啡豆4在罐子里,<br>咖啡豆5在罐子里,<br>咖啡豆6在罐子里,<br>咖啡豆7在罐子里,<br>\]<br>\]<br>\]|\[<br>\[<br>\[<br>\["Grasp", "Place"\],<br>\["Grasp", "Sweep"\],<br>\["Grasp", "Sweep"\],<br>\["Grasp", "Sweep"\],<br>\["Grasp", "Sweep"\],<br>\["Grasp", "Sweep"\],<br>\["Grasp", "Sweep"\],<br>\["Grasp", "Sweep"\]<br>\]<br>\]<br>\]|
||flip\_cup\_collect\_cookies|- \(0\.5\) 杯子杯口朝上<br>- \(0\.5 / 5\) 饼干1在碗里<br>- \(0\.5 / 5\) 饼干2在碗里<br>- \.\.\. \.\.\.<br>- \(0\.5 / 5\) 饼干5在碗里|杯子中心轴与World Z axis夹角在10°以内|\[<br>\[<br>\[<br>杯子杯口朝上,<br>饼干1在碗里,<br>饼干2在碗里,<br>饼干3在碗里,<br>饼干4在碗里,<br>饼干5在碗里,<br>\]<br>\]<br>\]|\[<br>\[<br>\[<br>\["Grasp", "Place", "Flip", "Handover"\],<br>\["Grasp", "Pour"\],<br>\["Grasp", "Pour"\],<br>\["Grasp", "Pour"\],<br>\["Grasp", "Pour"\],<br>\["Grasp", "Pour"\]<br>\]<br>\]<br>\]|
||frame\_against\_pen\_holder|- \(1/3\) 相框中心点保持一定高度（时序条件1：前置判断）<br>- \(1/3\) 相框靠近杯子（时序条件2）<br>- \(1/3\) 相框正且斜姿态（时序条件2）<br>|条件1是时序条件1，条件2和3并列为时序条件2<br>条件3要求相框法向量与World Z axis夹角在45°以内（以保证是斜靠姿态）|\[<br>\[<br>\[<br>相框中心点保持一定高度<br>\]<br>\],<br>\[<br>\[<br>相框靠近杯子,<br>相框正且斜姿态<br>\]<br>\]<br>\]|\[<br>\[<br>\[<br>\["Grasp", "Place"\]<br>\]<br>\],<br>\[<br>\[<br>\["Grasp", "Place", "Handover", "Flip"\],<br>\["Grasp", "Place", "Handover", "Flip"\]<br>\]<br>\]<br>\]|
||install\_gear|- \(1/2\) 齿轮放在轴上<br>- \(1/2\) 齿轮与另外两个齿轮耦合||\[<br>\[<br>\[<br>齿轮放在轴上,<br>齿轮与另外两个齿轮耦合<br>\]<br>\]<br>\]|\[<br>\[<br>\[<br>\["Grasp", "Place"\],<br>\["Grasp", "Place", "Press"\]<br>\]<br>\]<br>\]|
||peg\_in\_hole|- \(1/2\) 棍子离开原来孔洞<br>- \(1/2\) 棍子放入指定孔洞<br>|最终姿态要求：棍子与孔洞中心轴对齐，棍子插入孔洞一定距离，棍子保持竖直状态|\[<br>\[<br>\[<br>棍子离开原来孔洞,<br>棍子放入指定孔洞<br>\]<br>\]<br>\]|\[<br>\[<br>\[<br>\["Grasp", "Place"\],<br>\["Grasp", "Place", "Insert"\]<br>\]<br>\]<br>\]|
||put\_glass\_in\_glassbox|- \(1/3\) 两个镜腿折叠<br>- \(1/3\) 眼镜盒闭合<br>- \(1/3\) 眼镜在盒中|每个镜腿折叠至20°以内<br>对于条件3，只要眼镜在盒中即可，镜腿不折叠或眼镜盒未闭合也是可以的|\[<br>\[<br>\[<br>两个镜腿折叠,<br>眼镜盒闭合,<br>眼镜在盒中<br>\]<br>\]<br>\]|\[<br>\[<br>\[<br>\["Press"\],<br>\["Press"\],<br>\["Grasp", "Place"\]<br>\]<br>\]<br>\]|
||tighten\_nut|- \(1/2\) 螺母位于螺栓上端（时序条件1：前置判断）<br>- \(1/2\) 螺母完全旋入螺栓（时序条件2：满足上一条后再判断）<br>||\[<br>\[<br>\[<br>螺母位于螺栓上端<br>\]<br>\],<br>\[<br>\[<br>螺母完全旋入螺栓<br>\]<br>\]<br>\]|\[<br>\[<br>\[<br>\["Grasp", "Place"\]<br>\]<br>\],<br>\[<br>\[<br>\["Place", "Press"\]<br>\]<br>\]<br>\]|




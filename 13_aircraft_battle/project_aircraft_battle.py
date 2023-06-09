"""
    目标:
        1. 强化面向对象程序设计
        2. 体验使用pygame模块进行游戏开发
    实战步骤:
        1. pygame快速体验
        2. 飞机大战实战

    实现飞机大战主游戏类:
        plane_main ==> 游戏主程序
            封装主游戏类
            创建游戏对象
            启动游戏
        plane_sprites:
            封装游戏中所有需要使用到的精灵子类
            提供游戏的相关工具

    游戏的第一印象:
        1.把一些静止的图像绘制到游戏窗口中
        2.根据用户的交互或其他情况,移动这些图像,产生动画效果
        3.根据图像之间是否发生重叠,判断敌机是否被摧毁等其他情况

    使用pygame创建图形窗口
        目标:
            1. 游戏的初始化和退出
            2. 理解游戏中的坐标系
            3. 创建游戏主窗口
            4. 简单的游戏循环

    游戏的初始化和退出:
        1. 要使用pygame提供的所有功能之前, 需要调用init方法
            pygame.initial():导入并初始化所有pygame模块,使用其他模块之前,必须先调用init方法
        2.在游戏结束前需要调用一下quit方法
            pygame.quit():卸载所有pygame模块,在游戏结束之前调用
        具体语法:
            import pygame ==> 导入pygame, 模块
            pygame.init() ==> 游戏初始化
            pygame.quit() ==> 退出游戏

    游戏中的坐标系:
        1.原点在左上角(0,0)
        2.x轴水平方向向右,逐渐增加
        3.y轴垂直方向向下,逐渐增加
        4.在游戏中,所有可见元素都是以矩形区域来描述位置的
            要描述一个矩形区域有四个要素: (x, y), (width, height)
        5.pygame专门提供了一个类pygame.Rect用于描述矩形区域
            Rect(x, y, width, height) -> Rect(矩形对象)
            5.1 pygame.Rect类内部封装了一些数字计算
            5.2 pygame.Rect类不执行pygame.init()方法同样可以使用`
        案例需求
            1. 定义hero_rect矩形对象描述英雄的位置和大小
            2. 输出英雄的坐标原点(x和y)
            3. 输出英雄的尺寸(宽度和高度)

    创建游戏窗口-模块pygame.display用于创建和管理游戏窗口
        1.pygame.display.set_mode()方法:初始化游戏显示窗口
            1.1 set_mode()方法:
                set_mode(size(resolution)=(0, 0), flags=0, depth=0, display=0, vsync=0) ->Surface(返回值)
                作用:创建游戏显示窗口
            1.2 参数:
                resolution:指定屏幕的宽和高,默认创建的窗口大小和屏幕一致
                flags:指定屏幕的附加选项,例如是否全屏等,默认不需要传递
                depth:表示颜色的位数,默认自动匹配
            1.3 返回值:
                暂时可以理解为游戏的屏幕, 游戏的元素都需要被绘制到游戏的屏幕上
            1.4 注意: 必须使用变量记录 set_mode 方法的返回结果, 后续所有的图像绘制都基于这个返回结果
            1.5简单的游戏循环
                1.5.1 为了做到游戏启动后不会立即退出, 通常在游戏程序中增加一个游戏循环
                1.5.2 游戏循环就是一个无限循环
                1.5.3 在创建游戏窗口代码下方增加一个无限循环, 游戏窗口不需要重复创建
        2.pygame.display.update()方法: 刷新屏幕内容显示, 绘制图像后必须调用此方法才可以在屏幕显示绘制的图像

    理解图像并实现图像绘制
        1.在游戏中,能够看到的游戏元素大多是图像
            图像初始位置是保存在磁盘上的,需要先加载到内存中才可以使用
        2.要在屏幕上看到一个图像的内容,需要三个步骤:
            2.1 使用pygame.image.load(file_path)方法加载图像数据,用图像变量来接收返回结果
            2.2 使用游戏屏幕对象调用blit(图像变量,位置)方法将图像绘制到指定的位置
            2.3 调用pygame.display.update()方法更新整个屏幕的显示
            要想在屏幕上看到绘制的结果,必须要调用pygame.display.update()方法

    游戏中的动画实现原理
        1. 跟电影的原理类似, 游戏中的动画效果, 本质上是快速的在屏幕上绘制图像
        2. 一般在电脑上每秒绘制60次, 就能够达到连续的, 高品质的动画效果
           每次绘制的结果被称为帧Frame

    一个游戏主程序职责-游戏初始化和游戏循环
        游戏初始化:
            1.设置游戏窗口
            2.绘制图像初始位置
            3.设置游戏时钟
            4.创建精灵和精灵组
        游戏循环-游戏的正式开始:
            1.设置刷新频率
            2.检测用户交互: 事件监听, 碰撞检测
            3.更新所有图像位置 ==> 更新和绘制精灵组
            4.更新屏幕显示

    游戏时钟:
        1. pygame专门提供了一个类pygame.time.Clock, 可以非常方便的刷新屏幕绘制速度--刷新帧率
        2. 使用时钟对象的步骤:
            2.1 在游戏初始化创建一个时钟对象
            2.2 在游戏循环是让时钟对象调用tick(帧率)方法
        3. tick方法会根据上次被调用的时间, 自动设置游戏循环中的延时, 可以指定循环体内部代码的执行频率

    在游戏循环中监听事件:
        事件(event): 游戏启动后, 用户针对游戏所做的操作, 例如: 点击关闭按钮, 点击鼠标, 按下键盘
        监听: 在游戏循环中判断用户具体的操作, 只有捕获到用户具体的操作, 才能有针对性的做出响应
        代码实现:
            1.pygame中通过pygame.event.get()可以获得用户当前时刻动作的事件列表, 用户可以同一时间做很多事情
            2.这段代码非常固定, 几乎所有的pygame游戏都大同小异
                事件列表变量 = pygame.event.get()
                例: 判断用户点击关闭按钮事件的监听和处理
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print('退出游戏...')
                        pygame.quit()
                        exit()

    精灵(sprite)和精灵组:
        为了简化开发步骤, pygame提供了两个类
        1.pygame.sprite.Sprite ==> 精灵类(需要派生子类), 可创建存储图像数据image和位置rect的对象
            常用属性和方法:
                image: 记录图像数据
                rect: 记录在屏幕上的位置
                update(*args): 更新精灵位置
                kill(): 从所有组中删除
        2.pygame.Sprite.Group ==> 精灵组类
            常用属性和方法:
                __init__(self, *精灵)
                add(*sprites): 向组中增加精灵
                sprites:返回所有精灵列表
                update(*args):让组中所有精灵调用update方法
                draw(Surface):将组中所有精灵的image绘制到Surface的rect位置
        创建精灵和创建精灵组--游戏初始化
        精灵组.update()和精灵组.draw(screen)--游戏循环

    敌机出场
        需求:
            1.游戏启动后, 每隔一秒出现一架敌机
            2.每架敌机像屏幕下方飞行, 飞行速度各不相同
            3.每架敌机出现的水平位置不尽相同
            4.敌机从屏幕下方飞出, 不再飞回到屏幕中
        具体实现
            1.使用定时器添加敌机
                1.1 在pygame中可以使用pygame.time.set_timer()来添加定时器
                    定时器: 每隔一段时间, 去执行一些动作:
                        set_timer(eventid, millseconds) -> None
                1.2 set_timer()可以创建一个事件
                1.3 可以在游戏循环的时间监听方法中捕获到该事件
                1.4 定时器第一个参数事件代号需要基于常量pygame.USEREVENT来指定
                1.5 第二个参数是事件触发间隔的毫秒值
                1.6 定时器事件的监听:
                    1.6.1 通过pygame.event.get()获取当前时刻所有的事件列表
                    1.6.2 遍历列表并且判断event.type是否等于eventid, 如果相等, 表示定时器事件发生
                1.7 定义并监听创建敌机的定时器事件
                pygame的定时器使用套路:
                    01.定义定时器常量-eventid
                    02.再初始化方法中, 调用set_timer()方法设置定时器事件
                    03.在游戏循环中, 监听定时器事件
            2.设计Enemy类
                2.1 初始化方法:
                    指定敌机图片 ==> 随机指定敌机的初始位置和初始速度
                2.2 重写update方法:
                    判断敌机是否飞出屏幕, 如果是, 从精灵组删除

    英雄登场
        1.设计英雄和子弹类
        2.使用pygame.key.get_pressed()移动英雄
        3.发射子弹
        具体实现 ==> 设计英雄和子弹类:
            英雄需求:
                1.游戏启动后, 英雄出现在屏幕的水平中间位置, 距离屏幕底部120像素
                2.英雄每隔0.5秒发射一次子弹, 每次连发三枚子弹
                3.英雄默认不会移动, 需要通过控制方向键, 控制英雄移动
                    3.1. 判断event.type == pygame.KEYDOWN(需要按一次键盘, 英雄移动一次)
                        if event.type ==pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                            print('向右移动')
                    3.2. 可以按键不放使英雄一直移动:
                        3.2.1 首先使用pygame.key.get_pressed()返回所有按键的元组
                            keys_pressed = pygame.key.get_pressed()
                        3.2.2 通过键盘常量, 判断元组中某一个元素是否被按下--如果被按下, 对应数值为1
                            if keys_pressed[pygame.K_RIGHT]:
                                print('向右移动...')
            子弹需求:
                1.子弹从英雄的正上方发射沿直线向上方飞行
                2.飞出屏幕后要从精灵组删除
        Hero-英雄:
            a. 初始化方法:
                1. 指定英雄图片
                2. 初始速度=0,英雄默认静止不动
                3. 定义bullets子弹精灵组保存子弹精灵
            b. 重写update()方法:
                1. 英雄需要移动
                2. 并且需要保证不能移出屏幕
            c. 增加bullets属性, 记录所有子弹精灵
            d. 增加fire方法, 用于发射子弹
        Bullet-子弹:
            碰撞检测方法:
            1.pygame.sprite.groupcollide() ==> 两个精灵组中所有精灵的碰撞检测
                groupcollide(group1, group2, dokill1, dokill2, collided = None) -> Sprite_dict
                如果将dokill1设置为True, 则发生碰撞的精灵将被自动移除
                collide参数用于计算碰撞的的回调函数-若不指定, 则每个精灵必须有一个rect属性
            2.pygame.sprite.spritecollide() ==> 判断某个精灵和指定精灵组中的精灵碰撞
                spritecollide(sprite, group, dokill, collided = ) - Sprite_list
                若将dokill设置为True,则指定精灵组中发生碰撞的精灵将被自动移除
                collided参数用于计算碰撞的回调函数-若不指定,则每个精灵必须有一个rect属性
                返回精灵组中跟精灵发生碰撞的精灵列表
"""
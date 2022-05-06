# -*- coding: utf-8 -*-
import discord
from discord.ext.commands import Bot

TOKEN = ""

intents = discord.Intents.default()

bot = Bot(command_prefix='$', intents=intents)

# 임베드 메세지 만들기
@bot.command()
async def hello(ctx):
  embed = discord.Embed(title="환영합니다 드래곤레전드를 이용해주셔서 감사합니다. \n"
                              "다음의 명령어를 입력해주세요", description=
                        "!游戏无法安装\n"
                        "!无法更新\n"
                        "!a游戏中断并强制关闭\n"
                        "!i游戏中断并强制关闭\n"
                        "!玩游戏时画面会一直断开\n"
                        "!无法连接游戏该怎么做\n"
                        "!听不到背景音和效果音\n"
                        "!我想关闭背景音和效果音\n"
                        "!我想关闭背景音\n"
                        "!我想关闭效果音\n"
                        "!要关掉推送通知怎么办\n"
                        "!可以一边玩游戏一边听音乐吗\n"
                        "!想知道龙传奇游戏信息储存方法\n"
                        "!我不记得龙传奇账号和密码\n"
                        "!我丢失了龙传奇账号的密码丢失了\n"
                        "!如何更改游戏登录账号\n"
                        "!如果更换机器游戏信息会留下吗\n"
                        "!总是会显示连接其他机器的通知\n"
                        "!如果更换了机器或重新安装了游戏可以使用之前使用的账号吗\n"
                        "!可以删除游戏账号吗\n"
                        "!龙传奇的职员有问密码的情况吗\n"
                        "!用联动的账号登录却看不到角色\n"
                        "!google没有确认该账户是本人账户的信息和无法登录\n"
                        "!龙传奇会员注册在哪里\n"
                        "!无法加入龙传奇会员为什么呢\n"
                        "!龙传奇密码怎么变更\n"
                        "!据说新加入龙传奇的电子邮件地址已被用作其他账户的电子邮件地址\n"
                        "!邮件认证邮件未收到\n"
                        "!龙传奇会员怎么退出\n"
                        "!如何确认os信息\n"
                        "!执行龙传奇时因强制终止中断延迟现象很难使用\n"
                        "!无法访问龙传奇\n"
                        "!可以在海外进行游戏吗\n"
                        "!客户端安装及注册在哪里\n"
                        "!手机最低规格是多少\n"
                        "!因补丁错误而终止游戏请确认磁盘容量是否充足\n"
                        "!检测到未经批准的访问的信息和龙传奇将终止\n"
                        "!下载时设备不兼容此版本消息将会被曝光\n"
                        "!运行龙传奇后要求更新但未更新\n"
                        "!想要确认购买明细\n"
                        "!如何确认订购号码收据号码\n"
                        "!即使是同样的商品各商店的购买价格也不一样\n"
                        "!我想退货\n"
                        "!发生了结算错误\n"
                        "!购买的商品没有支付\n"
                        "!结算明细在哪里确认呢\n"
                        "!结算明细在哪里确认呢\n"
                        "!龙传奇的结算手段是什么\n"
                        "!已结算的商品不在邮箱里\n"
                        "!不小心使用了单品能修复吗\n"
                        "!dp的亮点是如何获得的在什么情况下使用的呢\n"
                        "!pop的亮点是如何获得的在什么情况下使用的呢\n"
                        "!xpop的亮点是如何获得的在什么情况下使用的呢\n"
                        "!dp的亮点消失了为什么那样\n"
                        "!pop的亮点消失了为什么那样\n"
                        "!xpop的亮点消失了为什么那样\n"
                        "!手机电池消耗太大了\n"
                        "!设置成静音也会发出声音\n"
                        "!设置成静音也会发出声音\n"
                        "!我不想收到推送信息\n"
                        "!听不到游戏的声音\n"
                        "!网络错误导致连接中断\n"
                        "!可以用手机游戏手柄控制器键盘鼠标使用龙传奇吗\n"
                        "!在哪里登记优惠券\n"
                        "!活动单品消失了\n"
                        "!中奖了怎么获取\n"
                        "!优惠券补偿如何发放\n"
                        "!怎么获得龙蛋和龙\n"
                        "!龙蛋龙怎么升级\n"
                        "!龙等级\n"
                        "!龙蛋等级\n"
                        "!如何提升技能呢\n"
                        "!一般技能和特别技能是什么\n"
                        "!龙总共进化几个阶段\n"
                        "!想知道财物的种类\n"
                        "!我想详细的了解一下龙蛋\n"
                        "!我想详细的了解龙的能力值\n"
                        "!想删除佣兵该怎么做\n"
                        "!佣兵在哪里使用\n"
                        "!我想增加最大体力的最大值\n"
                        "!好友代养陪玩功能是什么\n"
                        "!体力如何恢复\n"
                        "!鸟巢如何进行扩张\n"
                        "!在哪里可以购买管理工具药水\n"
                        "!想知道龙孵化的概率的信息\n"
                        "!不可以在电脑端上下载吗\n"
                        "!现在支持什么语言呢\n"
                        "!游戏昵称设置过一次可以再更改吗\n"
                        "!画面看着太亮或者太暗非常累现在游戏里面可以调节亮度吗\n"
                        "!推荐人邀请的方法出了微信二维码还有别的方法吗\n"
                        "!游戏可以录像吗\n"
                        "!如何生成钱包呢\n"
                        "!dp积分里如何换成pop积分呢\n"
                        "!从哪里可以确定积分呢\n")


  await ctx.send(embed=embed)


@bot.event
async def on_ready():
   print(f'로그인 성공: {bot.user}')

@bot.command()
async def hi(ctx):
    await ctx.reply("Hello World!")



# 특정 명령어 입력시 관련 문구 출력

@bot.command()
async def 游戏无法安装(ctx):
  await ctx.reply("如未安装游戏，请确认是否收到符合设备的文件或确认存储空间的容量。")

@bot.command()
async def 无法更新(ctx):
  await ctx.reply("如无法更新，请在网络环境顺畅的位置上再次尝试。")

@bot.command()
async def a游戏中断并强制关闭(ctx):
  await ctx.reply("如果游戏使用过程中画面持续中断,请重新安装应用程序或重新启动机器后重新运行。 如果问题持续下去，请通过（支持邮件）进行咨询。")

@bot.command()
async def i游戏中断并强制关闭(ctx):
  await ctx.reply("如果游戏使用过程中画面持续中断,请重新安装应用程序或重新启动机器后重新运行。 如果问题持续下去，请通过（支持邮件）进行咨询。")

@bot.command()
async def 玩游戏时画面会一直断开(ctx):
  await ctx.reply("如果游戏使用过程中画面持续中断,请重新安装应用程序或重新启动机器后重新运行。 如果问题持续下去，请通过（支持邮件）进行咨询。")

@bot.command()
async def 无法连接游戏该怎么做(ctx):
  await ctx.reply("如果无法连接游戏,请确认是否已经连接网络。 如果问题持续下去，请通过（支持邮件）进行咨询。")

@bot.command()
async def 听不到背景音和效果音(ctx):
  await ctx.reply("如果听不到背景音和效果音，请确认电脑的音量是否已经静音。\n或者在选项中存在静音时，请解除该静音。")

@bot.command()
async def 我想关闭背景音和效果音(ctx):
  await ctx.reply("如果听不到背景音和效果音，请确认电脑的音量是否已经静音。或者在选项中存在静音时，请解除该静音。")

@bot.command()
async def 我想关闭背景音(ctx):
  await ctx.reply("想要关闭背景音时，可以在选项中使用静音功能。")

@bot.command()
async def 我想关闭效果音(ctx):
  await ctx.reply("想要关闭效果音时，可以在选项中使用静音功能。")

@bot.command()
async def 要关掉推送通知怎么办(ctx):
  await ctx.reply("推送通知可从选项中解禁")

@bot.command()
async def 可以一边玩游戏一边听音乐吗(ctx):
  await ctx.reply("播放该音乐的应用程序支持PIP时,可以一边播放龙传奇一边播放该音乐。")

@bot.command()
async def 想知道龙传奇游戏信息储存方法(ctx):
  await ctx.reply("游戏信息通过网络将账户信息存储在服务器上。")

@bot.command()
async def 我不记得龙传奇账号和密码(ctx):
  await ctx.reply("账户与正在使用的邮箱地址相同。 密码在知道正在使用的电子邮件时，可通过（支持邮件）重新设置密码。")

@bot.command()
async def 我丢失了龙传奇账号的密码丢失了(ctx):
  await ctx.reply("如果知道正在使用的电子邮件，通过（支持邮件）进行咨询，就可以重新设置密码。")

@bot.command()
async def 如何更改游戏登录账号(ctx):
  await ctx.reply("在选项中，您可以通过退出登录， 登录其他账号， 在该机器上更改登录账号")

@bot.command()
async def 如果更换机器游戏信息会留下吗(ctx):
  await ctx.reply("即使变更机器,如果知道现有的账户信息,也可以通过相关信息在其他机器上连接播放。")

@bot.command()
async def 总是会显示连接其他机器的通知(ctx):
  await ctx.reply("龙传奇 规定一个账户同时只能在一个机器上连接。 如果您在其他设备上连接，请在该设备上注销。")

@bot.command()
async def 如果更换了机器或重新安装了游戏可以使用之前使用的账号吗(ctx):
  await ctx.reply("可以。 如果您知道该账户的账号和密码， 您可以重新登录使用。")

@bot.command()
async def 可以删除游戏账号吗(ctx):
  await ctx.reply("原则上不支持删除游戏账号，通过（支持邮件）进行咨询，将删除相应游戏账号。")

@bot.command()
async def 龙传奇的职员有问密码的情况吗(ctx):
  await ctx.reply("龙传奇职员绝对不会询问顾客的密码。 询问密码时，绝对不是职员，请立即通过（支持邮件）举报。")

@bot.command()
async def 用联动的账号登录却看不到角色(ctx):
  await ctx.reply("请确认一下是否用您想要的账号登录。 如需登录所需账号，如发生相应现象，请通过（支持邮件）进行咨询。")

@bot.command()
async def google没有确认该账户是本人账户的信息和无法登录(ctx):
  await ctx.reply("在多个机器上试图登录时可能会发生。 请通过谷歌账号客服中心进行咨询")

@bot.command()
async def 龙传奇会员注册在哪里(ctx):
  await ctx.reply("龙传奇会员注册可以通过游戏内的程序进行")

@bot.command()
async def 无法加入龙传奇会员为什么呢(ctx):
  await ctx.reply("输入的邮件已经使用时，不加入会员。 如有其他问题，请通过（支持邮件）进行咨询。")

@bot.command()
async def 龙传奇密码怎么变更(ctx):
  await ctx.reply("密码变更可通过URL进行变更，如通过（支持邮件）进行咨询，则可以通过URL进行密码变更。")

@bot.command()
async def 据说新加入龙传奇的电子邮件地址已被用作其他账户的电子邮件地址(ctx):
  await ctx.reply("在其他账户上使用相应电子邮件时，可通过密码登录相应账户或认为被盗用时，可通过（支持邮件）进行咨询。")

@bot.command()
async def 邮件认证邮件未收到(ctx):
  await ctx.reply("如未收到电子邮件，则有可能被转移到垃圾邮件保管箱中，请确认。 如果垃圾箱里也没有，请重新申请认证邮件。")

@bot.command()
async def 龙传奇会员怎么退出(ctx):
  await ctx.reply("会员退出在政策上不能在游戏内进行,请通过(支持邮件)要求会员退出。")

@bot.command()
async def 如何确认os信息(ctx):
  await ctx.reply("Android的情况是，在设置应用程序进入手机信息-软件信息后，可以确认Android版本\n" +
                  "iOS的情况是，从设置应用程序移动到一般项目后，进入信息菜单即可确认软件版本")

@bot.command()
async def 执行龙传奇时因强制终止中断延迟现象很难使用(ctx):
  await ctx.reply("如果游戏使用过程中画面持续中断,请重新安装应用程序或重新启动机器后重新运行。 如果问题持续下去，请通过（支持邮件）进行咨询。")

@bot.command()
async def 无法访问龙传奇(ctx):
  await ctx.reply("如果无法连接游戏,请确认是否已经连接网络。 如果问题持续下去，请通过（支持邮件）进行咨询。")

@bot.command()
async def 可以在海外进行游戏吗(ctx):
  await ctx.reply("中国版本只能在中国国内游戏，通过全球版本可以在海外游戏。")

@bot.command()
async def 客户端安装及注册在哪里(ctx):
  await ctx.reply("客户端的安装可在主页顶部的下载链接中接收文件后安装，会员注册可在游戏内通过会员注册程序进行。")

@bot.command()
async def 手机最低规格是多少(ctx):
  await ctx.reply("Android是Android 5.0以上，iOS是最新OS（2022-03-14基准iOS 15）。")

@bot.command()
async def 因补丁错误而终止游戏请确认磁盘容量是否充足(ctx):
  await ctx.reply("在进行安装之前，请确认机器是否有足够的存储空间。 建议容量在512MB以上。")

@bot.command()
async def 检测到未经批准的访问的信息和龙传奇将终止 (ctx):
  await ctx.reply("如果机器被套路或实施越狱,则可以在其他应用程序上任意访问龙传奇,因此可能会发生这种情况。 请尽量通过正式的固件实行。")

@bot.command()
async def 下载时设备不兼容此版本消息将会被曝光(ctx):
  await ctx.reply("这可能发生在机器的操作系统过时或机器不兼容时。 请安装最新操作系统,并参考支援机型。")

@bot.command()
async def 运行龙传奇后要求更新但未更新(ctx):
  await ctx.reply("机器没有剩余空间时可能会发生。 请删除不必要的文件，确保空间后再尝试。")

@bot.command()
async def 想要确认购买明细(ctx):
  await ctx.reply("购买明细通过（支持邮件）进行咨询的话，提供可以阅览加入账户购买明细的URL。")

@bot.command()
async def 如何确认订购号码收据号码(ctx):
  await ctx.reply("订单号码/收据号码可通过加入的邮件在发送收据上确认。")

@bot.command()
async def 即使是同样的商品各商店的购买价格也不一样(ctx):
  await ctx.reply("因为各商店的价格政策不同,所以为了遵守这一规定,龙传奇不得不对购买价格有所差异。")

@bot.command()
async def 我想退货(ctx):
  await ctx.reply("想要退款时，请勿使用所购买的商品，并附上通过邮件发送的收据，通过（支持邮件）进行咨询。")

@bot.command()
async def 发生了结算错误(ctx):
  await ctx.reply("发生结算错误时，相应结算手段存在问题，请确认余额及检查时间。")

@bot.command()
async def 购买的商品没有支付(ctx):
  await ctx.reply("结算的商品通过邮箱支付。 如果邮箱里也没有的话，请通过（支持邮件）进行咨询。")

@bot.command()
async def 结算明细在哪里确认呢(ctx):
  await ctx.reply("收据可以通过加入的邮件确认。")

@bot.command()
async def 龙传奇的结算手段是什么(ctx):
  await ctx.reply("龙传奇的结算手段有Kakao Pay、微信支付、信用卡。")

@bot.command()
async def 已结算的商品不在邮箱里(ctx):
  await ctx.reply("如果已结算的商品不在邮箱，请稍等片刻后再确认。 如果以后也没能继续领取,请通过(支持邮件)进行咨询。")

@bot.command()
async def 不小心使用了单品能修复吗(ctx):
  await ctx.reply("原则上使用商品时，不另行修复。 但因网络错误而使用后仍未能取得使用结果时，可通过（支持邮件）确认后恢复使用。")

@bot.command()
async def dp的亮点是如何获得的在什么情况下使用的呢(ctx):
  await ctx.reply("请参考手册的财物文段")

@bot.command()
async def pop的亮点是如何获得的在什么情况下使用的呢(ctx):
  await ctx.reply("请参考手册的财物文段")

@bot.command()
async def xpop的亮点是如何获得的在什么情况下使用的呢(ctx):
  await ctx.reply("请参考手册的财物文段")

@bot.command()
async def dp的亮点消失了为什么那样(ctx):
  await ctx.reply("因为XPOP与钱包相连,所以钱包中使用的XPOP量可能会同步消失。 如果相关财物未使用也消失的话，请通过（支持邮件）进行咨询。")

@bot.command()
async def pop的亮点消失了为什么那样(ctx):
  await ctx.reply("因为XPOP与钱包相连,所以钱包中使用的XPOP量可能会同步消失。 如果相关财物未使用也消失的话，请通过（支持邮件）进行咨询。")

@bot.command()
async def xpop的亮点消失了为什么那样(ctx):
  await ctx.reply("因为XPOP与钱包相连,所以钱包中使用的XPOP量可能会同步消失。 如果相关财物未使用也消失的话，请通过（支持邮件）进行咨询。")

@bot.command()
async def 手机电池消耗太大了(ctx):
  await ctx.reply("如果运行多个后台应用，电池消耗量可能会增加。 请重新启动手机，重新运行。\n" + "如果该现象持续下去，请通过（支持邮件）进行咨询。" )

@bot.command()
async def 设置成静音也会发出声音(ctx):
  await ctx.reply("请确认选项中是否设置了静音 。 \n 如果已经静音了也能听到的话,请通过(支持邮件)进行咨询。")

@bot.command()
async def 我不想收到推送信息(ctx):
  await ctx.reply("推送通知可从选项中解禁。")

@bot.command()
async def 听不到游戏的声音(ctx):
  await ctx.reply("请确认机器音量是否静音。 或者请确认选项中声音是否静音。")

@bot.command()
async def 网络错误导致连接中断(ctx):
  await ctx.reply("建议在网络畅通的地方进行游戏。")

@bot.command()
async def 可以用手机游戏手柄控制器键盘鼠标使用龙传奇吗(ctx):
  await ctx.reply("龙传奇不支持单独的外部控制器。")

@bot.command()
async def 在哪里登记优惠券(ctx):
  await ctx.reply("优惠券登记可在优惠券输入页面输入账户信息和优惠券号码。")

@bot.command()
async def 活动单品消失了(ctx):
  await ctx.reply("如果中了游戏奖励却未能领取或消失的话,请通过(支持邮件)进行咨询。")

@bot.command()
async def 中奖了怎么获取(ctx):
  await ctx.reply("对于游戏奖励,在中奖公告后,将尽快通过邮件进行奖励。 现货补偿的情况，通过加入的邮件发送确认配送地的邮件，敬请参考。")

# @bot.command()
# async def 쿠폰입력오류(ctx):
#   await ctx.reply("iOS의 경우에는 정책상 인게임에서 쿠폰을 입력할 수 없습니다. 별도의 쿠폰입력 페이지를 통해 입력하여 주시길 바랍니다.")

@bot.command()
async def 优惠券补偿如何发放(ctx):
  await ctx.reply("优惠券补偿通过邮件支付,如果在支付30天内不领取,就不能领取优惠券。")

# @bot.command()
# async def 이벤트당첨(ctx):
#   await ctx.reply("인게임 보상의 경우에는 당첨 공지 이후 빠른 시일내로 우편을 통해 보상이 지급됩니다. 현물 보상의 경우에는 가입하신 메일을 통해 배송지 확인을 위한 메일을 보내드리니 참고바랍니다.")

@bot.command()
async def 怎么获得龙蛋和龙(ctx):
  await ctx.reply("龙蛋在最初注册会员后发放，在商店也可以购买。 龙可以通过孵化龙蛋获得。")

@bot.command()
async def 龙蛋龙怎么升级(ctx):
  await ctx.reply("龙蛋/龙 升级可累计获得培养经验值。")

@bot.command()
async def 龙等级(ctx):
  await ctx.reply("龙等级包括免费支付（普通话），共分为7个阶段，根据R的购买价格区分等级。")

@bot.command()
async def 龙蛋等级(ctx):
  await ctx.reply("龙蛋等级包括免费支付，共分为7个阶段，根据龙蛋的购买价格区分等级")

@bot.command()
async def 如何提升技能呢(ctx):
  await ctx.reply("技能升级在实施一定次数的技能培养时即可。")

@bot.command()
async def 一般技能和特别技能是什么(ctx):
  await ctx.reply("一般技能作为完成补偿,支付成长经验值、DP,特别技能在此基础上追加支付龙的特定能力值")

@bot.command()
async def 龙总共进化几个阶段(ctx):
  await ctx.reply("龙由龙蛋-幼龙-小龙-成体龙阶段组成")

@bot.command()
async def 想知道财物的种类(ctx):
  await ctx.reply("财物是由DP, POP, XPOP积分构成.")

@bot.command()
async def 我想详细的了解一下龙蛋(ctx):
  await ctx.reply("龙蛋的能力值在购买超声波检查仪后使用即可确认.")

@bot.command()
async def 我想详细的了解龙的能力值(ctx):
  await ctx.reply("龙的能力值可在鸟巢选择龙后通过能力值菜单确认。")

@bot.command()
async def 想删除佣兵该怎么做(ctx):
  await ctx.reply("想要删除佣兵时，可以在鸟巢选择用兵后，通过销售按钮将其贩卖来进行删除。")

@bot.command()
async def 佣兵在哪里使用(ctx):
  await ctx.reply("外援给龙角色当食物使用时，龙的特定能力值会上升。 或者在PvP内容中龙数量不足时,可以代替位置用于战斗。")

@bot.command()
async def 我想增加最大体力的最大值(ctx):
  await ctx.reply("每次账户级别达到一定级别时， 体力最大值都会增加。")

@bot.command()
async def 好友代养陪玩功能是什么(ctx):
  await ctx.reply("好友代养是代替培养朋友的龙蛋/龙的功能，如果朋友要求的话，\n 自己的巢穴里有空隙的话，可以带过来代替培养，获得补偿。代替好友陪玩,而是使用培养的龙蛋/龙玩的功能获得成长经验值的行为。")

@bot.command()
async def 体力如何恢复(ctx):
  await ctx.reply("体力每30分钟自动恢复1次，使用体力药水，可立即恢复最大体力值。")

@bot.command()
async def 鸟巢如何进行扩张(ctx):
  await ctx.reply("鸟巢可以通过在商店购买鸟巢扩展项目来扩展额外的鸟巢槽。")

@bot.command()
async def 在哪里可以购买管理工具药水(ctx):
  await ctx.reply("管理工具、药水可在主菜单上，在商店-商品项目上购买。")

@bot.command()
async def 想变更龙蛋龙的名字(ctx):
  await ctx.reply("想要更改龙蛋/龙的名称时，可在鸟巢选择相应龙蛋/龙后，按下名称右边的按钮来更改名称。")

@bot.command()
async def 任务一天最多可以进行几次(ctx):
  await ctx.reply("任务是每日任务的情况下一天最多可完成4次。 每周任务的情况下一周最多可完成4次")

@bot.command()
async def 龙蛋龙的角色名上标有颜色在什么状态下显示(ctx):
  await ctx.reply("角色名称的颜色根据龙蛋/龙的等级来区分，并不意味着状态异常。")

@bot.command()
async def 任务没有完成(ctx):
  await ctx.reply("任务尚未完成时，请确认是否满足该任务的完成条件。 \n如果满足完成条件却未完成的情况，请通过（支持邮件）进行咨询。")

@bot.command()
async def 下一次更新是在什么时候呢(ctx):
  await ctx.reply("更新相关日程通过相关公告定期进行公告。")

@bot.command()
async def 对于游戏有一些反馈想发送要发到哪里呢(ctx):
  await ctx.reply("对游戏的反馈希望在 (支持邮箱)里咨询.")

@bot.command()
async def 在玩游戏的时候发现了错误要往哪里申报呢(ctx):
  await ctx.reply("游戏里发现错误的情况 希望在(支持邮箱)里咨询.")

@bot.command()
async def 想知道龙孵化的概率的信息(ctx):
  await ctx.reply("龙孵化的概率通过 (外部概率票链接)可以确认.")

@bot.command()
async def 不可以在电脑端上下载吗(ctx):
  await ctx.reply("龙传奇不支持电脑下载.")

@bot.command()
async def 现在支持什么语言呢(ctx):
  await ctx.reply("龙传奇支持中文和英文")

@bot.command()
async def 游戏昵称设置过一次可以再更改吗(ctx):
  await ctx.reply("游戏昵称设置过一次之后不能再更改了")

@bot.command()
async def 画面看着太亮或者太暗非常累现在游戏里面可以调节亮度吗(ctx):
  await ctx.reply("游戏里面不可以调节亮度， 您可以用调整设备的亮度来代替.")

@bot.command()
async def 推荐人邀请的方法出了微信二维码还有别的方法吗(ctx):
  await ctx.reply("推荐人现在除了微信二维码不提供其他的办法")

@bot.command()
async def 游戏可以录像吗(ctx):
  await ctx.reply("游戏内不直接提供录制功能.")

@bot.command()
async def 如何生成钱包呢(ctx):
  await ctx.reply("钱包可以通过XETA 软件生成. 龙传奇支持这个联动功能.")

@bot.command()
async def dp积分里如何换成pop积分呢(ctx):
  await ctx.reply("公开页面里可以看到的部分所以跳过")

@bot.command()
async def 从哪里可以确定积分呢(ctx):
    await ctx.reply("积分可以在主界面的UI商谈或者我的信息里确定")

# 임베드 만들기


# 봇 실행 코드
bot.run(TOKEN)


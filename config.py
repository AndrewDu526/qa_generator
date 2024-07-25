# GPT3.5 提示词
input_from = '''
                几个理想的问答示例将在之后给出
                例子：  
                {example}

                问题和回答绝对不要出现文本来源内容
                按照理想问题示例，必须含有对应的“[问题]”和“[回答]”标签
                请先对文本生成几个总结性的问答
                请生成尽可能多的问答来评估对以下文本的了解
                请仅提供问答
                若提供的信息不充分请不要生成问答
                绝对不要生成没有正面回答的无意义问答，下面是一个反面例子：
                
                [问题]:在GB/T 17820-1999标准中，提供了哪方面关于天然气的规范？ 
                [回答]:GB/T 17820-1999标准提供了关于天然气的规范。


                文本：
                {text}
             '''
# 问题样例
examples = '''
              [问题]:信号输出方式主要包括哪些类型？[回答]:信号输出方式主要包括脉冲、模拟量或数字通信方式。
              [问题]:旋进漩涡流是如何产生的？[回答]:旋进漩涡流是由旋涡发生器强制使气流产生旋涡流，然后在文丘利管中旋进，到达收缩段时突然节流使旋涡流加速，最终进入扩散段后因回流作用产生二次旋涡流。
              [问题]:对于电子显示装置的流量计输出装置，应该显示哪些信息？[回答]:当为电子显示装置时, 应可显示通过流量计的总量和瞬时流量。流量的计量单位应清晰地标志在显示装置的适当位置。
              [问题]:元数据实体是什么？[回答]:元数据实体是一组可以说明数据相同特性的元数据元素。
              [提问]:测量系统一般包含哪些组件？  [回答]:测量系统一般包含计算重量或体积的数字传感器、计算价格的通用计算机和打印测量值及付费价格的打印机。
          '''

system_text = '你是一现在你将根据我给你的说明书片段文本中提出问题和回答，以评估燃气公司员工对燃气器械相关知识的熟悉程度'
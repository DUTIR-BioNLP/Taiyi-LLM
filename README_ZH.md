[ [English](./README.md) | **中文** \]

<p align="center">
    <br>
    <img src="./fig/logo-all.png?raw=true" width="800" height="381"/>
    <br>
</p>

<p align="center">
        🤗 <a href="https://huggingface.co/DUTIR-BioNLP/Taiyi2-chat">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/models/DUTIRbionlp/Taiyi2-chat">ModelScope<a>&nbsp&nbsp | &nbsp&nbsp🖥️ <a href="https://modelscope.cn/studios/DUTIRbionlp/Taiyi2_Demo">Demo</a>&nbsp&nbsp | &nbsp&nbsp🗂️<a href="./data_file/dataset_inf.md">Data</a>&nbsp&nbsp | &nbsp&nbsp📃 <a href="https://academic.oup.com/jamia/article/31/9/1865/7616487?utm_source=authortollfreelink&utm_campaign=jamia&utm_medium=email&guestAccessKey=4c56c223-a555-4949-bef7-16e77f8baa10">Paper</a>&nbsp&nbsp | &nbsp&nbsp<a href="https://mp.weixin.qq.com/s/HlyzalsxdNy6yFV2iGqbBQ">WeChat (微信)</a> 
<br>
<br>
</p>

# 太一（Taiyi）：基于多任务指令微调的中英双语生物医学大模型

**项目背景**

随着深度学习技术的迅速发展，类ChatGPT、DeepSeek等大语言模型在自然语言处理领域已经取得了显著的进展。面向生物医学领域，大语言模型有助于医生与患者之间的沟通，提供有用的医学信息，并在辅助诊疗、生物医学知识发现、药物研发、个性化医疗方案等方面具有巨大潜力。因此，本项目开展了面向生物医学多场景的多语多任务大模型的研究，目标实现高性能、低资源耗费的生物医学领域大模型，于2023年10月发布初版中英双语生物医学大模型——[太一（Taiyi）](https://github.com/DUTIR-BioNLP/Taiyi-LLM/tree/Taiyi1)，并持续开展研究，目前完成太一2研发，进行模型开源。

## 太一2主要更新

相比于太一1模型，太一2主要在模型基座、数据指令、任务指令等方面进行了进一步的研究和更新，主要更新如下：

- **更新基座**： 太一2从原始的Qwen-7B基座更新为GLM4-9B
- **高质量数据筛选**：根据数据集标注指南，进一步的进行了数据质量筛选，删除了低质量数据量，并对不同任务的数据配比进行了调整，将极度不平衡的数据进行了平衡。
- **任务指令精细化**：按任务类型划分，进行实验测试不同任务指令构建方法，设计出精细化的任务最佳指令数据构建方式。

## 太一2性能指标

太一2在13个生物医学任务测试数据集上进行了测试，结果如下图。

<p align="center">
    <br>
    <img src="./fig/taiyi2_performance.png?raw=true" width="800" height="499"/>
    <br>
</p>

在生物医学任务数据集上，实验结果表明：

- 太一2平均指标相比太一1提升约9%。
- 太一2平均指标相比通用领域GPT3.5、DeepSeek14B蒸馏版提升约25%。
- 太一2平均指标获得了和目前领域先进专用模型可竞争的结果。

具体指标如下表：

<table >
<tr>
  <th>任务类型</th>
  <th>数据集</th>
  <th>太一1</th>
  <th>太一2</th>
  <th>GPT3.5</th>
  <th>DeepSeek-14B</th>
  <th>SOTA</th>  
</tr>
<tr>
  <td rowspan = '5'>实体识别(Micro-F1)</th>
  <td>BC5CDR-Chem</td>
  <td align="center">80.2</td>
  <td align="center">90.2</td>
  <td align="center">60.3</td>
  <td align="center">42.3</td>
  <td align="center">93.3(PubMedBERT)</td>  
</tr>
<tr>
  <td>BC5CDR-Dise</td>
  <td align="center">69.1</td>
  <td align="center">78.3</td>
  <td align="center">51.8</td>
  <td align="center">41.1</td>
  <td align="center">85.6(PubMedBERT)</td>  
</tr>
<tr>
  <td>CHEMDNER</td>
  <td align="center">79.9</td>
  <td align="center">90.5</td>
  <td align="center">36.5</td>
  <td align="center">43.3</td>
  <td align="center">92.4(BioBERT)</td>  
</tr>
<tr>
  <td>NCBIdisease</td>
  <td align="center">73.1</td>
  <td align="center">82.6</td>
  <td align="center">50.5</td>
  <td align="center">32.8</td>
  <td align="center">87.8(PubMedBERT)</td>  
</tr>
<tr>
  <td>CMeEE-dev</td>
  <td align="center">65.7</td>
  <td align="center">74.1</td>
  <td align="center">47.0</td>
  <td align="center">42.4</td>
  <td align="center">74.0(CBLUE)</td>  
</tr>
<tr>
  <td rowspan = '2'>关系抽取(Micro-F1)</th>
  <td>BC5CDR</td>
  <td align="center">37.5</td>
  <td align="center">42.4</td>
  <td align="center">14.2</td>
  <td align="center">28.6</td>
  <td align="center">45.0(BioGPT)</td>  
</tr>
<tr>
  <td>CMeIE-dev</td>
  <td align="center">43.2</td>
  <td align="center">50.3</td>
  <td align="center">30.6</td>
  <td align="center">4.5</td>
  <td align="center">54.9(CBLUE)</td>  
</tr>
<tr>
  <td rowspan = '3'>文本分类(Micro-F1)</th>
  <td>BC7LitCovid</td>
  <td align="center">84.0</td>
  <td align="center">90.2</td>
  <td align="center">63.9</td>
  <td align="center">32.9</td>
  <td align="center">91.8(Bioformer)</td>  
</tr>
<tr>
  <td>HOC</td>
  <td align="center">80.0</td>
  <td align="center">84.6</td>
  <td align="center">51.2</td>
  <td align="center">41.9</td>
  <td align="center">82.3(PubMedBERT)</td>  
</tr>
<tr>
  <td>KUAKE_QIC-dev</td>
  <td align="center">77.4</td>
  <td align="center">80.4</td>
  <td align="center">48.5</td>
  <td align="center">47.5</td>
  <td align="center">85.9(CBLUE)</td>  
</tr>
<tr>
  <td rowspan = '3'>填空问答(Accuracy)</th>
  <td>PubMedQA</td>
  <td align="center">54.4</td>
  <td align="center">58.8</td>
  <td align="center">76.5</td>
  <td align="center">46.4</td>
  <td align="center">73.4</td>  
</tr>
<tr>
  <td>MedQA-USMLE</td>
  <td align="center">37.1</td>
  <td align="center">58.4</td>
  <td align="center">51.3</td>
  <td align="center">66.9</td>
  <td align="center">42.0</td>  
</tr>
<tr>
  <td>MedQA-MCMLE</td>
  <td align="center">64.8</td>
  <td align="center">88.1</td>
  <td align="center">58.2</td>
  <td align="center">53.2</td>
  <td align="center">70.1(RoBERTA-large)</td>  
</tr>
<tr>
  <td>全部</th>
  <td>均值AVE</td>
  <td align="center">65.1</td>
  <td align="center">74.5</td>
  <td align="center">49.3</td>
  <td align="center">40.3</td>
  <td align="center">75.3</td>  
</tr>
</table>

## 模型使用

### 环境搭建

本项目训练和测试使用的环境配置如下：

```
torch==2.4.0
ms_swift==2.6.1
transformers==4.44.0
transformers-stream-generator==0.0.5
vllm==0.6.0
vllm-flash-attn==2.6.1
```

可使用如下命令按照环境包：

```
$ pip install -r requirements.txt
```

### 模型推理

参考`taiyi2_chat.py`文件，为了保证推理速度，建议使用GPU显卡。


## 开发团队

太一2由[大连理工大学信息检索研究室（DUTIR）](http://ir.dlut.edu.cn/)开发完成。

指导教师：[罗凌](http://faculty.dlut.edu.cn/luoling/zh_CN/index.htm)、王健、孙媛媛、林鸿飞

学生成员：汪志军、祁杰蔚、李俊涛、吕腾啸、刘超、袁浩斌

## 致谢

本项目的工作受到以下开源项目与技术的启发和帮助，在此对相关项目和研究开发人员表示感谢，包括但不限于：

- GLM: https://github.com/THUDM/GLM-4
- SWIFT: https://github.com/modelscope/ms-swift
- BigBIO: https://github.com/bigscience-workshop/biomedical
- PromptCBLUE: https://github.com/michael-wzhu/PromptCBLUE
- 太一logo 由文心一言AI合成

## 免责声明

本项目相关资源仅供学术研究之用，严禁用于商业用途。对本仓库源码的使用遵循开源许可协议 [Apache 2.0](https://github.com/DUTIR-BioNLP/Taiyi-LLM/blob/main/LICENSE)。在使用过程中，用户需认真阅读并遵守以下声明：

1. 请您确保您所输入的内容未侵害他人权益，未涉及不良信息，同时未输入与政治、暴力、色情相关的内容，且所有输入内容均合法合规。
2. 请您确认并知悉使用太一大模型生成的所有内容均由人工智能模型生成，生成内容具有不完全理性，本项目对其生成内容的准确性、完整性和功能性不做任何保证，亦不承担任何法律责任。
3. 本模型中出现的任何违反法律法规或公序良俗的回答，均不代表本项目的态度、观点或立场，本项目将不断完善模型回答以使其更符合社会伦理和道德规范。
4. 对于模型输出的任何内容，使用者需自行承担风险和责任，本项目不承担任何法律责任，亦不对因使用相关资源和输出结果而可能产生的任何损失承担责任。
5. 本项目中出现的第三方链接或库仅为提供便利而存在，其内容和观点与本项目无关。使用者在使用时需自行辨别，本项目不承担任何连带责任；
6. 若使用者发现项目出现任何重大错误，请向我方反馈，以助于我们及时修复。

使用本项目即表示您已经仔细阅读、理解并同意遵守以上免责声明。本项目保留在不预先通知任何人的情况下修改本声明的权利。

## 引用

如果你使用到了本项目的仓库，请引用。

```
@article{Taiyi,
  title="{Taiyi: A Bilingual Fine-Tuned Large Language Model for Diverse Biomedical Tasks}",
  author={Ling Luo, Jinzhong Ning, Yingwen Zhao, Zhijun Wang, Zeyuan Ding, Peng Chen, Weiru Fu, Qinyu Han, Guangtao Xu, Yunzhi Qiu, Dinghao Pan, Jiru Li, Hao Li, Wenduo Feng, Senbo Tu, Yuqi Liu, Zhihao Yang, Jian Wang, Yuanyuan Sun, Hongfei Lin},
  journal={Journal of the American Medical Informatics Association},
  year={2024},
  doi = {10.1093/jamia/ocae037},
  url = {https://doi.org/10.1093/jamia/ocae037},
}
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=DUTIR-BioNLP/Taiyi-LLM&type=Date)](https://star-history.com/#DUTIR-BioNLP/Taiyi-LLM&Date)


[ **English** | [中文](./README_ZH.md) \]

<p align="center">
    <br>
    <img src="./fig/logo-all.png?raw=true" width="800" height="381"/>
    <br>
</p>

<p align="center">
        🤗 <a href="https://huggingface.co/DUTIR-BioNLP/Taiyi2-chat">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/models/DUTIRbionlp/Taiyi2-chat">ModelScope<a>&nbsp&nbsp | &nbsp&nbsp🖥️ <a href="https://modelscope.cn/studios/DUTIRbionlp/Taiyi2_Demo">Demo</a>&nbsp&nbsp | &nbsp&nbsp🗂️<a href="./data_file/dataset_inf.md">Data</a>&nbsp&nbsp | &nbsp&nbsp📃<a href="https://academic.oup.com/jamia/article/31/9/1865/7616487?utm_source=authortollfreelink&utm_campaign=jamia&utm_medium=email&guestAccessKey=4c56c223-a555-4949-bef7-16e77f8baa10">Paper</a>&nbsp&nbsp| &nbsp&nbsp <a href="https://mp.weixin.qq.com/s/HlyzalsxdNy6yFV2iGqbBQ">WeChat (微信)</a> 
<br>
<br>
</p>

# Taiyi (太一): A Bilingual (Chinese and English) Fine-Tuned Large Language Model for Diverse Biomedical Tasks

**Project Background**

With the rapid development of deep learning technology, large language models (LLMs) like ChatGPT and DeepSeek have made significant progress in the field of natural language processing. In the biomedical domain, large language models can facilitate communication between doctors and patients, provide useful medical information, and hold great potential in areas such as clinical decision support, biomedical knowledge discovery, drug development, and personalized treatment planning. Therefore, this project focuses on developing a multilingual, multi-task large language model tailored for various biomedical scenarios, aiming to achieve high performance with low resource consumption. In October 2023, we released the initial version of a bilingual Chinese-English biomedical large language model—[Taiyi](https://github.com/DUTIR-BioNLP/Taiyi-LLM/tree/Taiyi1). Research efforts have continued, and the development of Taiyi 2 has now been completed, with the model being open-sourced.

## Major Updates in Taiyi 2

Compared to the Taiyi 1, Taiyi 2 introduces further research and improvements in areas such as the model backbone, data instructions, and task-specific instructions. The main updates are as follows:

* ​**Updated Backbone**​: Taiyi 2 replaces the original Qwen-7B backbone with GLM4-9B.
* ​**High-Quality Data Filtering**​: Based on dataset annotation guidelines, data quality has been further refined by removing low-quality samples. Additionally, the data distribution across different tasks has been rebalanced to address extreme imbalances.
* ​**Refined Task Instructions**​: Tasks are categorized by type, and experimental testing was conducted to evaluate various instruction construction methods. This led to the development of a refined, task-optimized instruction design strategy.

## Performance of Taiyi 2

Taiyi 2 was evaluated on 13 biomedical task benchmark datasets, with results shown in the figure below.

<p align="center">
    <br>
    <img src="./fig/taiyi2_performance.png?raw=true" width="800" height="499"/>
    <br>
</p>

On these biomedical datasets, the experimental results show that:

- Taiyi 2 achieves an average performance improvement of approximately 9% over Taiyi 1.
- Compared to general-domain models such as GPT-3.5 and the distilled version of DeepSeek-14B, Taiyi 2 shows an average improvement of around 25%.
- Taiyi 2 achieves competitive results comparable to the current state-of-the-art domain-specific models.

Detailed metrics are presented in the table below:

<table >
<tr>
  <th>Task Type</th>
  <th>Dataset</th>
  <th>Taiyi1</th>
  <th>Taiyi2</th>
  <th>GPT3.5</th>
  <th>DeepSeek-14B</th>
  <th>SOTA</th>  
</tr>
<tr>
  <td rowspan = '5'>NER (Micro-F1)</th>
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
  <td rowspan = '2'>RE (Micro-F1)</th>
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
  <td rowspan = '3'>TC (Micro-F1)</th>
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
  <td rowspan = '3'>QA (Accuracy)</th>
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
  <td>All</th>
  <td>AVE</td>
  <td align="center">65.1</td>
  <td align="center">74.5</td>
  <td align="center">49.3</td>
  <td align="center">40.3</td>
  <td align="center">75.3</td>  
</tr>
</table>

## Model Usage

### Environment Setup

The environment configuration we used for training and testing is as follows:

```
torch==2.4.0
ms_swift==2.6.1
transformers==4.44.0
transformers-stream-generator==0.0.5
vllm==0.6.0
vllm-flash-attn==2.6.1
```

To install all dependencies automatically using the command:

```
$ pip install -r requirements.txt
```

### Model Inference

Referring to the `taiyi2_chat.py` file, it is recommended to use a GPU to ensure faster inference speed.

## Development Team

Taiyi 2 was developed by the [Dalian University of Technology Information Retrieval Research Laboratory（DUTIR）](http://ir.dlut.edu.cn/)

Supervisors: [Ling Luo](http://faculty.dlut.edu.cn/luoling/en/index.htm), Jian Wang, Yuanyuan Sun, Hongfei Lin

Student Members: Zhijun Wang, Jiewei Qi, Juntao Li, Tengxiao Lv, Chao Liu, Haobin Yuan

## Acknowledgements

The work of this project has been inspired and assisted by the following open-source projects and technologies. We would like to express our gratitude to the developers and contributors of these projects, including but not limited to:

- GLM: https://github.com/THUDM/GLM-4
- SWIFT: https://github.com/modelscope/ms-swift
- BigBIO: https://github.com/bigscience-workshop/biomedical
- PromptCBLUE: https://github.com/michael-wzhu/PromptCBLUE
- The Taiyi logo was synthesized by ERNIE Bot

## Disclaimer

The resources related to this project are for academic research purposes only and are strictly prohibited from commercial use. The use of the source code of this warehouse follows the open source license agreement [Apache 2.0](https://github.com/DUTIR-BioNLP/Taiyi-LLM/blob/main/LICENSE).
During use, users are required to carefully read and comply with the following statements:

1. Please ensure that the content you input does not infringe on the rights and interests of others, does not involve harmful information, and does not contain any content related to politics, violence, or pornography, and all input content is legal and compliant.
2. Please confirm and be aware that all content generated using the Taiyi model is generated by artificial intelligence models, and the generated content is not entirely rational. This project does not guarantee the accuracy, completeness, and functionality of the generated content, nor assumes any legal responsibility.
3. Any responses that violate laws, regulations, public order, or good customs in this model do not represent the attitude, viewpoint, or stance of this project. This project will continuously improve the model responses to make them more in line with social ethics and moral norms.
4. For any content output by the model, the user shall bear their own risks and responsibilities. This project does not assume any legal responsibility, nor shall they be liable for any losses that may arise from the use of relevant resources and output results.
5. The third-party links or libraries appearing in this project are for convenience only, and their content and viewpoints are not related to this project. Users need to distinguish themselves when using, and this project does not assume any joint liability;
6. If users discover any significant errors in the project, please provide feedback to us to help us fix them in a timely manner.

By using this project, you have carefully read, understood, and agreed to abide by the above disclaimer. This project reserves the right to modify this statement without prior notice to anyone.

## Citation

If you use the repository of this project, please cite it.

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


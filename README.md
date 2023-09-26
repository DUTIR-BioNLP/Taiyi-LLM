[ **English** | [中文](./README_ZH.md) \]
<p align="center">
    <br>
    <img src="./fig/logo-all.png?raw=true" width="800" height="381"/>
    <br>
</p>


<p align="center">
        🤗 <a href="https://huggingface.co/Qwen">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/models/qwen">ModelScope<a>&nbsp&nbsp | &nbsp&nbsp🖥️ <a href="https://modelscope.cn/studios/qwen/Qwen-14B-Chat-Demo/summary">Demo</a>&nbsp&nbsp | &nbsp&nbsp<a href="assets/wechat.png">WeChat (微信)</a>
<br>
<br>
</p>

# Taiyi (太一)：Bilingual Biomedical Large Language Model in Chinese and English

**Project Background**

With the rapid development of deep learning technology, large language models like ChatGPT have made significant progress in the field of natural language processing. In the context of biomedical applications, large language models facilitate communication between healthcare professionals and patients, provide valuable medical information, and have enormous potential in assisting diagnosis, biomedical knowledge discovery, drug development, and personalized healthcare solutions, among others. However, in the AI community, there is a relative scarcity of existing open-source biomedical large models, with most of them primarily focused on monolingual medical question-answering dialogues in either Chinese or English. Therefore, this project embarks on research dedicated to large models for the biomedical domain and introduces the initial version of a bilingual Chinese-English biomedical large model named 'Taiyi', iming to explore the capabilities of large models in handling a variety of Chinese-English natural language processing tasks in the biomedical field.


**Project Highlights**

- **Abundant Biomedical Training Resources**：For the biomedical domain, this project has collected and organized a diverse set of Chinese-English biomedical Natural Language Processing (BioNLP) training datasets. This collection includes a total of 38 Chinese datasets covering 10 BioNLP tasks and 131 English datasets covering 12 BioNLP tasks. To facilitate task-specific requirements, standardized data formats have been designed and applied for consistent formatting across all datasets.
- **Exceptional Bilingual BioNLP Multi-Task Capability in Chinese and English**：Designing and constructing a bilingual Chinese-English instruction dataset (comprising over 1 million samples) for large model fine-tuning, enabling the model to excel in various BioNLP tasks including intelligent biomedical question-answering, doctor-patient dialogues, report generation, information extraction, machine translation, headline generation, text classification, and more.
- **Open Source Information**：Open-source Chinese-English BioNLP dataset curation details, Taiyi large model weights, and model inference deployment scripts.

**Overview of Framework**

<p align="center">
    <br>
    <img src="./fig/overview_en.png?raw=true" width="800" height="451"/>
    <br>
</p>

## Contents
- [Taiyi (太一)：Bilingual Biomedical Large Language Model in Chinese and English](#taiyi-太一bilingual-biomedical-large-language-model-in-chinese-and-english)
  - [Contents](#contents)
  - [Main Functions](#main-functions)
    - [1. Question Answering](#1-question-answering)
    - [2. Doctor-Patient Dialogue](#2-doctor-patient-dialogue)
    - [3. Medical Report Generation](#3-medical-report-generation)
    - [4. Biomedical Information Extraction](#4-biomedical-information-extraction)
      - [4.1 Named Entity Recognition](#41-named-entity-recognition)
      - [4.2 Relation Extraction](#42-relation-extraction)
      - [4.3 Event Extraction](#43-event-extraction)
    - [5. Machine Translation](#5-machine-translation)
    - [6. Title Generation](#6-title-generation)
    - [7. Text Classification](#7-text-classification)
    - [8. Text Semantic Similarity](#8-text-semantic-similarity)
  - [Training Data](#training-data)
    - [Data Collection](#data-collection)
    - [Standardized Data Format](#standardized-data-format)
    - [Instruction-Tuning Data](#instruction-tuning-data)
  - [模型训练](#模型训练)
  - [模型部署](#模型部署)
  - [Limitation and Future Work](#limitation-and-future-work)
  - [Development Team](#development-team)
  - [Acknowledgements](#acknowledgements)
  - [Disclaimer](#disclaimer)
  - [Citation](#citation)
  - [Star History](#star-history)



## Main Functions
### 1. Question Answering
**Task Introduction**

Biomedical question answering is designed to assist users in obtaining answers and information related to the field of biomedical science through a question-and-answer format. It contributes to more effective management of biomedical information, enhances the quality of medical decision-making, and improves the effectiveness of biomedical education.

<details>
  <summary><b>Examples</b></summary>

**Example in Chinese**

**Input：** 我最近感到头晕和恶心，这可能是什么原因？

```
头晕和恶心可以有多种原因，包括感冒、中耳炎、低血糖、贫血等。为了获得确切的答案，建议咨询医生进行详细检查。
```

**Example in English**

**Input：** 我最近感到头晕和恶心，这可能是什么原因？

```
头晕和恶心可以有多种原因，包括感冒、中耳炎、低血糖、贫血等。为了获得确切的答案，建议咨询医生进行详细检查。
```
</details>

### 2. Doctor-Patient Dialogue
**Task Introduction**

The Taiyi model is capable of simulating natural language conversations between doctors and patients. These conversations can encompass various biomedical topics, including medical inquiries, disease prevention, medication consultations, and more.

<details>
  <summary><b>Examples</b></summary>

**Example in Chinese**

```
用户：我最近感到头痛和喉咙痛。
太一：我很抱歉听到您不舒服。可以告诉我头痛和喉咙痛的症状持续多久了吗？
用户：我最近感到头痛和喉咙痛。
太一：我很抱歉听到您不舒服。可以告诉我头痛和喉咙痛的症状持续多久了吗？
```

**Example in English**

```
用户：我最近感到头痛和喉咙痛。
太一：我很抱歉听到您不舒服。可以告诉我头痛和喉咙痛的症状持续多久了吗？
用户：我最近感到头痛和喉咙痛。
太一：我很抱歉听到您不舒服。可以告诉我头痛和喉咙痛的症状持续多久了吗？
```
</details>

### 3. Medical Report Generation
**Task Introduction**

Medical report auto-generation aims to summarize information during the diagnostic process. The task requires the language model to generate medical reports in a specified format based on patient self-reports and doctor-patient dialogues. This task can assist doctors in handling a large volume of medical information more effectively and provide accurate diagnoses and treatment recommendations to patients.

<details>
  <summary><b>Examples</b></summary>

**Example in Chinese**

**User inputs：** 
```
根据对话，生成医疗报告：

患者：你好，医生。我最近总是感觉头疼，尤其是在用电脑工作后。

医生：你好，我很抱歉听到你不舒服。头疼的感觉是怎样的？是持续性的还是阵发性的？

患者：它更像是阵发性的，特别是在我长时间盯着电脑屏幕后。

医生：我明白了。你在工作或者休息的时候有没有定期休息和做眼保健操？

患者：我试过，但并没有太大的帮助。

医生：我明白了。这可能是由于用眼过度导致的，建议你尝试调整一下工作习惯，比如每隔一小时休息一下，远眺一下远处的风景。如果症状持续不减或者加重，建议你去医院进行进一步的检查。

患者：好的，谢谢你，医生。
```
**Taiyi outputs：**  
```   
患者姓名：未知
日期：未知
主诉：
     患者报告在使用电脑工作后经常感到头疼，症状呈阵发性，尤其在长时间盯着电脑屏幕后。
     临床观察：
     患者试过定期休息和做眼保健操，但并没有太大的帮助。
     初步诊断：
     可能是由于用眼过度导致的头疼。
     建议：
     1. 调整工作习惯，比如每隔一小时休息一下，远眺一下远处的风景。
     2. 如果症状持续不减或者加重，建议去医院进行进一步的检查。

     注意：这只是一个基本的报告，并不能代替真正的医疗咨询。如果你有任何健康问题，建议你寻求专业医生的帮助。
```    
**Example in English**

**User inputs：** 
```
根据对话，生成医疗报告：

患者：你好，医生。我最近总是感觉头疼，尤其是在用电脑工作后。

医生：你好，我很抱歉听到你不舒服。头疼的感觉是怎样的？是持续性的还是阵发性的？

患者：它更像是阵发性的，特别是在我长时间盯着电脑屏幕后。

医生：我明白了。你在工作或者休息的时候有没有定期休息和做眼保健操？

患者：我试过，但并没有太大的帮助。

医生：我明白了。这可能是由于用眼过度导致的，建议你尝试调整一下工作习惯，比如每隔一小时休息一下，远眺一下远处的风景。如果症状持续不减或者加重，建议你去医院进行进一步的检查。

患者：好的，谢谢你，医生。
```
**Taiyi outputs：**  
```   
患者姓名：未知
日期：未知
主诉：
     患者报告在使用电脑工作后经常感到头疼，症状呈阵发性，尤其在长时间盯着电脑屏幕后。
     临床观察：
     患者试过定期休息和做眼保健操，但并没有太大的帮助。
     初步诊断：
     可能是由于用眼过度导致的头疼。
     建议：
     1. 调整工作习惯，比如每隔一小时休息一下，远眺一下远处的风景。
     2. 如果症状持续不减或者加重，建议去医院进行进一步的检查。

     注意：这只是一个基本的报告，并不能代替真正的医疗咨询。如果你有任何健康问题，建议你寻求专业医生的帮助。
```    
</details>

### 4. Biomedical Information Extraction
#### 4.1 Named Entity Recognition
**Task Introduction**

Biomedical named entity recognition aims to identify predefined biomedical entities from text. These entities can include biomedical concepts such as diseases, drugs, genes, proteins, and more.

<details>
  <summary><b>Examples</b></summary>

**Example in Chinese**

**User input：** 
``` 
请从下面的文本中提取医疗实体：

主要病理改变为脑实质和脑膜水肿、充血，微小血管出血，尤以大脑海马、延髓、脑桥、小脑和咬伤部位相应的背根节及脊髓段最为严重。
``` 
**Taiyi output：**
``` 
     "身体": "脑实质", "脑膜", "大脑海马", "延髓", "脑桥", "小脑", "背根节", "脊髓段"
     
     "临床表现": "脑实质和脑膜水肿、充血" 
     
     "疾病": "微小血管出血"
``` 

**Example in English**

**User input：** 
``` 
请从下面的文本中提取医疗实体：

主要病理改变为脑实质和脑膜水肿、充血，微小血管出血，尤以大脑海马、延髓、脑桥、小脑和咬伤部位相应的背根节及脊髓段最为严重。
``` 
**Taiyi output：**
``` 
     "身体": "脑实质", "脑膜", "大脑海马", "延髓", "脑桥", "小脑", "背根节", "脊髓段"
     
     "临床表现": "脑实质和脑膜水肿、充血" 
     
     "疾病": "微小血管出血"
``` 
</details>

#### 4.2 Relation Extraction
**Task Introduction**

Biomedical relationship extraction aims to automatically extract relationships or associations between biomedical entities from text, such as interactions between proteins and genes, therapeutic relationships between drugs and diseases, and more.

<details>
  <summary><b>Examples</b></summary>

**Example in Chinese**

**User input：** 
``` 
请从下面的文本中提取医疗实体：

主要病理改变为脑实质和脑膜水肿、充血，微小血管出血，尤以大脑海马、延髓、脑桥、小脑和咬伤部位相应的背根节及脊髓段最为严重。
``` 
**Taiyi output：**
``` 
     "身体": "脑实质", "脑膜", "大脑海马", "延髓", "脑桥", "小脑", "背根节", "脊髓段"
     
     "临床表现": "脑实质和脑膜水肿、充血" 
     
     "疾病": "微小血管出血"
``` 

**Example in English**

**User input：** 
``` 
请从下面的文本中提取医疗实体：

主要病理改变为脑实质和脑膜水肿、充血，微小血管出血，尤以大脑海马、延髓、脑桥、小脑和咬伤部位相应的背根节及脊髓段最为严重。
``` 
**Taiyi output：**
``` 
     "身体": "脑实质", "脑膜", "大脑海马", "延髓", "脑桥", "小脑", "背根节", "脊髓段"
     
     "临床表现": "脑实质和脑膜水肿、充血" 
     
     "疾病": "微小血管出血"
``` 
</details>


#### 4.3 Event Extraction
**Task Introduction**

The goal of biomedical event extraction is to extract structured biomedical events from unstructured and vast biomedical literature, mining the described biological entities in the literature, as well as the fine-grained relationships between biomedical events. This task can save time in manually reviewing literature and provide support for the construction of relevant databases, disease diagnosis, prevention research, and more.

<details>
  <summary><b>Examples</b></summary>

**Example in Chinese**

**User input：** 
``` 
请从下面的文本中提取医疗实体：

主要病理改变为脑实质和脑膜水肿、充血，微小血管出血，尤以大脑海马、延髓、脑桥、小脑和咬伤部位相应的背根节及脊髓段最为严重。
``` 
**Taiyi output：**
``` 
     "身体": "脑实质", "脑膜", "大脑海马", "延髓", "脑桥", "小脑", "背根节", "脊髓段"
     
     "临床表现": "脑实质和脑膜水肿、充血" 
     
     "疾病": "微小血管出血"
``` 

**Example in English**

**User input：** 
``` 
请从下面的文本中提取医疗实体：

主要病理改变为脑实质和脑膜水肿、充血，微小血管出血，尤以大脑海马、延髓、脑桥、小脑和咬伤部位相应的背根节及脊髓段最为严重。
``` 
**Taiyi output：**
``` 
     "身体": "脑实质", "脑膜", "大脑海马", "延髓", "脑桥", "小脑", "背根节", "脊髓段"
     
     "临床表现": "脑实质和脑膜水肿、充血" 
     
     "疾病": "微小血管出血"
``` 
</details>


### 5. Machine Translation

**Task Introduction**

Machine translation can convert biomedical texts from one natural language to another. This task can assist in translating various medical questions and recommendations, disease names, symptoms, and other information between English and Chinese, for example.

<details>
  <summary><b>Examples</b></summary>

**Chinese to English Translation Example**

**User input：** 
``` 
请从下面的文本中提取医疗实体：

主要病理改变为脑实质和脑膜水肿、充血，微小血管出血，尤以大脑海马、延髓、脑桥、小脑和咬伤部位相应的背根节及脊髓段最为严重。
``` 
**Taiyi output：**
``` 
     "身体": "脑实质", "脑膜", "大脑海马", "延髓", "脑桥", "小脑", "背根节", "脊髓段"
     
     "临床表现": "脑实质和脑膜水肿、充血" 
     
     "疾病": "微小血管出血"
``` 

**English to Chinese Translation Example**

**User input：** 
``` 
请从下面的文本中提取医疗实体：

主要病理改变为脑实质和脑膜水肿、充血，微小血管出血，尤以大脑海马、延髓、脑桥、小脑和咬伤部位相应的背根节及脊髓段最为严重。
``` 
**Taiyi output：**
``` 
     "身体": "脑实质", "脑膜", "大脑海马", "延髓", "脑桥", "小脑", "背根节", "脊髓段"
     
     "临床表现": "脑实质和脑膜水肿、充血" 
     
     "疾病": "微小血管出血"
``` 
</details>


### 6. Title Generation

**Task Introduction**

Title generation aims to generate informative article titles for input biomedical text paragraphs with summarization.

<details>
  <summary><b>Examples</b></summary>

**Example in Chinese**

**User input：** 
``` 
请从下面的文本中提取医疗实体：

主要病理改变为脑实质和脑膜水肿、充血，微小血管出血，尤以大脑海马、延髓、脑桥、小脑和咬伤部位相应的背根节及脊髓段最为严重。
``` 
**Taiyi output：**
``` 
     "身体": "脑实质", "脑膜", "大脑海马", "延髓", "脑桥", "小脑", "背根节", "脊髓段"
     
     "临床表现": "脑实质和脑膜水肿、充血" 
     
     "疾病": "微小血管出血"
``` 

**Example in English**

**User input：** 
``` 
请从下面的文本中提取医疗实体：

主要病理改变为脑实质和脑膜水肿、充血，微小血管出血，尤以大脑海马、延髓、脑桥、小脑和咬伤部位相应的背根节及脊髓段最为严重。
``` 
**Taiyi output：**
``` 
     "身体": "脑实质", "脑膜", "大脑海马", "延髓", "脑桥", "小脑", "背根节", "脊髓段"
     
     "临床表现": "脑实质和脑膜水肿、充血" 
     
     "疾病": "微小血管出血"
``` 
</details>

### 7. Text Classification

**Task Introduction**

Biomedical text classification aims to automatically categorize biomedical texts into predefined class labels, aiding healthcare professionals, researchers, and institutions in better managing and analyzing medical information.

<details>
  <summary><b>Examples</b></summary>

**Example in Chinese**

**User input：** 
``` 
请从下面的文本中提取医疗实体：

主要病理改变为脑实质和脑膜水肿、充血，微小血管出血，尤以大脑海马、延髓、脑桥、小脑和咬伤部位相应的背根节及脊髓段最为严重。
``` 
**Taiyi output：**
``` 
     "身体": "脑实质", "脑膜", "大脑海马", "延髓", "脑桥", "小脑", "背根节", "脊髓段"
     
     "临床表现": "脑实质和脑膜水肿、充血" 
     
     "疾病": "微小血管出血"
``` 

**Example in English**

**User input：** 
``` 
请从下面的文本中提取医疗实体：

主要病理改变为脑实质和脑膜水肿、充血，微小血管出血，尤以大脑海马、延髓、脑桥、小脑和咬伤部位相应的背根节及脊髓段最为严重。
``` 
**Taiyi output：**
``` 
     "身体": "脑实质", "脑膜", "大脑海马", "延髓", "脑桥", "小脑", "背根节", "脊髓段"
     
     "临床表现": "脑实质和脑膜水肿、充血" 
     
     "疾病": "微小血管出血"
``` 
</details>

### 8. Text Semantic Similarity
**Task Introduction**

Text Semantic Similarity aims to determine the degree of association or similarity between two medical texts. This task typically involves text matching, similarity measurement, and semantic understanding and can be used in various applications such as medical information retrieval and document matching.

<details>
  <summary><b>Examples</b></summary>

**Example in Chinese**

**User input：** 
``` 
请从下面的文本中提取医疗实体：

主要病理改变为脑实质和脑膜水肿、充血，微小血管出血，尤以大脑海马、延髓、脑桥、小脑和咬伤部位相应的背根节及脊髓段最为严重。
``` 
**Taiyi output：**
``` 
     "身体": "脑实质", "脑膜", "大脑海马", "延髓", "脑桥", "小脑", "背根节", "脊髓段"
     
     "临床表现": "脑实质和脑膜水肿、充血" 
     
     "疾病": "微小血管出血"
``` 

**Example in English**

**User input：** 
``` 
请从下面的文本中提取医疗实体：

主要病理改变为脑实质和脑膜水肿、充血，微小血管出血，尤以大脑海马、延髓、脑桥、小脑和咬伤部位相应的背根节及脊髓段最为严重。
``` 
**Taiyi output：**
``` 
     "身体": "脑实质", "脑膜", "大脑海马", "延髓", "脑桥", "小脑", "背根节", "脊髓段"
     
     "临床表现": "脑实质和脑膜水肿、充血" 
     
     "疾病": "微小血管出血"
``` 
</details>

## Training Data

### Data Collection
To fully leverage existing biomedical natural language processing datasets, this project collected a total of 170 open-source datasets in both Chinese and English. Among these, there are 38 Chinese datasets covering 10 BioNLP tasks and 131 English datasets covering 12 BioNLP tasks. An overview of the datasets is provided in the following figure.

<p align="center">
    <br>
    <img src="./fig/data_overview-2.png?raw=true" width="1096" height="400"/>
    <br>
</p>

This project compiled information on each dataset, including task type, data scale, task description, and relevant data links. For specific details, please refer to the ["Overview of the Biomedical Datasets"](./data_file/dataset_inf.md).

### Standardized Data Format
To facilitate subsequent data conversion, this project drew inspiration from the [BigBio](https://github.com/bigscience-workshop/biomedical) project and, based on the type of tasks, devised a unified data format. For specific details about this standardized data format, please refer to the ["DUTIR-BioNLP Data Schema Documentation"](./data_file/Task_schemas_en.md), and the data has been transformed to adhere to this standardized format.

### Instruction-Tuning Data
After filtering and selecting datasets based on data quality, instructional templates were designed and data was transformed according to the standardized data format. The summary of the instruction-tuning data is presented in the following table:


<table >
<tr>
  <th>Task Type</th>
  <th>Chinese Data Scale</th>
  <th>English Data Scale</th>
</tr>
<tr>
  <td>Named Entity Recognition</td>
  <td>44,667</td>
  <td>28,603</td>
</tr>
<tr>
  <td>Relation Extraction</td>
  <td>26,606</td>
  <td>17,279</td>
</tr>
<tr>
  <td>Event Extraction</td>
  <td>2,992</td>
  <td>2,022</td>
</tr>
<tr>
  <td>Text Classification</td>
  <td>37,624</td>
  <td>40,339</td>
</tr>
<tr>
  <td>Text Pair Task</td>
  <td>45,548</td>
  <td>11,237</td>
</tr>
<tr>
  <td>Machine Translation</td>
  <td colspan ="2"; align="center">74,113</td>
</tr>
<tr>
  <td>Single-turn Question and Answer</td>
  <td>129,562</td>
  <td>57,962</td>
</tr>
<tr>
  <td>Multi-Round Dialogue</td>
  <td>16,391</td>
  <td>10,000</td>
</tr>
<tr>
  <td>Multi-Round Dialogue</td>
  <td>16,391</td>
  <td>10,000</td>
</tr>
<tr>
  <td>Other Additional Tasks</td>
  <td colspan ="2"; align="center">9,370</td>
</tr>
<tr>
  <td>General Chain-of-Thought Data</td>
  <td>50,000</td>
  <td>7,473</td>
</tr>
<tr>
  <td>General Dialogue Data</td>
  <td colspan ="2"; align="center">390,000</td>
</tr>
<tr>
  <td>Total</td>
  <td colspan ="2"; align="center">1,001,788</td>
</tr>
</table>

For detailed information on the instructional data used for training, please refer to the ["Instruction-Tuning Data Details"](./data_file/final_instruction_data.md).


## 模型训练

## 模型部署


## Limitation and Future Work

**Limitations**

The goal of this project is to explore the Chinese English bilingual natural language processing capabilities of the large model in the biomedical field. However, there are some shortcomings that must be considered in Taiyi model at present:

- Misunderstanding: Like all major language models, there is a risk of misunderstanding or misinterpretation, especially when dealing with specialized terminology or complex concepts in the biomedical field. In this case, our model may provide inaccurate answers or explanations.

- Hallucinations: Large language models sometimes generate meaningless or completely unrelated responses to a given input. This' hallucination 'may be particularly problematic when users are unfamiliar with the discussion topic, as they may not be able to easily identify errors in the model output.

- Limited Information: Despite our commitment to becoming a comprehensive language model in the biomedical field, the knowledge of the model is still limited and may not cover all aspects of each field or profession. Users should be aware that the information in the model may not be comprehensive and use it with caution when in-depth or professional knowledge is needed.

- Bias: The training data of the model may contain biases, which may be reflected in the model's response. We strive to reduce bias, but we cannot completely eliminate it. Users should handle potential bias issues in model responses with caution.

Note: The Taiyi model is intended to provide information and knowledge, but should not be used as a substitute for medical professionals' advice or diagnosis. Any decision involving personal health should be consulted with professional medical personnel.

**Future Work**

- Open source data and technical manuscripts: Organize and improve data resources and model training technical manuscripts, and will be released as open source in the future.

- Continuing pretraining: Due to current computing resource limitations, the current version of Taiyi mainly performs instruction data fine-tuning and does not use massive biomedical resources to continue pretraining. In the future, this project will explore the use of large model bases in the biomedical field resources to futher pretraining.

- Reinforcement learning enhances performance: This project will explore how to further enhance the performance of models and align human intentions using reinforcement learning methods.

- Enhanced interpretability: Compared to the general field, the biomedical field requires higher interpretability of model prediction results. In the future, we will explore the interpretability methods of Taiyi on various BioNLP tasks.

- Enhanced security: Although security data has been added for training in this project, model security in the biomedical field is still insufficient. We will continue to explore how to use biomedical knowledge bases to enhance model security.
  
- ......

## Development Team
Taiyi was developed by the [Dalian University of Technology Information Retrieval Research Laboratory（DUTIR）](http://ir.dlut.edu.cn/) 

Supervisors: [Ling Luo](http://faculty.dlut.edu.cn/luoling/en/index.htm), Zhihao Yang, Jian Wang, Yuanyuan Sun, Hongfei Lin

Student Members: Jinzhong Ning, Yingwen Zhao, Zeyuan Ding, Peng Chen, Weiru Fu, Qinyu Han, Guangtao Xu, Yunzhi Qiu, Dinghao Pan, Jiru Li, Zhijun Wang, Hao Li, Wenduo Feng, Senbo Tu, Yuqi Liu


## Acknowledgements
The work of this project has been inspired and assisted by the following open-source projects and technologies. We would like to express our gratitude to the developers and contributors of these projects, including but not limited to:
- Qwen: https://github.com/QwenLM/Qwen
- BigBIO: https://github.com/bigscience-workshop/biomedical
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
@misc{taiyi,
    author = {Taiyi-Team}.
    title = {Taiyi: A Biomedical Large Language Model Finetuned with Rich Bilingual Biomedical Data}
    year = {2023},
    publisher = {GitHub},
    journal = {GitHub repository}
    howpublished = {\url{https://github.com/DUTIR-BioNLP/Taiyi-LLM}}
}
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=DUTIR-BioNLP/Task_schemas&type=Date)](https://star-history.com/#DUTIR-BioNLP/Task_schemas&Date)


 
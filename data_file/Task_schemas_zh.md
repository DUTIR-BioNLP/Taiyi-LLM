


# DUTIR BioNLP数据统一格式
本项目在[BigBio](https://github.com/bigscience-workshop/biomedical)项目基础上，定义了一组轻量级、任务特定的数据统一格式，以帮助简化对常见生物医学数据集的编程访问。

## 目录
- [DUTIR BioNLP数据统一格式](#dutir-bionlp数据统一格式)
  - [目录](#目录)
  - [信息抽取（Information Extraction，IE）](#信息抽取information-extractionie)
    - [文本段落](#文本段落)
    - [实体（NER/NEN）](#实体nernen)
    - [关系（RE）](#关系re)
    - [因果关系（CRE）](#因果关系cre)
    - [事件（EE）](#事件ee)
    - [指代消解（COREF）](#指代消解coref)
  - [文本分类（Text Classification，TC）](#文本分类text-classificationtc)
  - [问答（Question Answering，QA）](#问答question-answeringqa)
    - [多项选择（Multiple Choice， multiple\_choice）](#多项选择multiple-choice-multiple_choice)
    - [简单问答（Simple Answer Questions，sqa）](#简单问答simple-answer-questionssqa)
    - [基于上下文问答（Context-based Answer Questions，cqa）](#基于上下文问答context-based-answer-questionscqa)
  - [多轮对话（Multi-Round Dialogue，MRD）](#多轮对话multi-round-dialoguemrd)
  - [机器翻译（Machine Translation，MT）](#机器翻译machine-translationmt)
  - [文本对（Text Pairs，TP）](#文本对text-pairstp)
    - [文本蕴含（Textual Entailment，te）](#文本蕴含textual-entailmentte)
    - [语义相似度计算（Semantic Similarity，ss）](#语义相似度计算semantic-similarityss)
  - [文本到文本/结构（Text to Text/Struct，TT）](#文本到文本结构text-to-textstructtt)
    - [文本摘要（Document Summarization，ds）](#文本摘要document-summarizationds)
    - [文本到结构（Text to Struct，ts）](#文本到结构text-to-structts)

## 信息抽取（Information Extraction，IE）

这是一种简单的容器格式，具有最少的嵌套，支持一系列信息抽取任务：

- 命名实体识别（Named entity recognition，NER） (**Example: Chinese/CMeEE-V2**) 和实体链接/标准化（Named entity normalization/linking，NEN）  (**Example:English/ncbi_disease**)
- 关系抽取（Relation extraction，RE） (**Example: Chinese/CMeIE-V2**)
- 因果关系抽取（Causal relation extraction，CRE）
- 事件（Event extraction，EE） 
- 指代消解（Coreference resolution，COREF）

```
{
    "id": "ABCDEFG",
    "document_id": "XXXXXX",
    "passages": [...],
    "entities": [...],
    "events": [...],
    "coreferences": [...],
    "relations": [...],
}
```



**格式说明**

- `id` 字段出现在顶部（即文档）级别。它们以“0”开头，这使得数据集中的每个`id`字段都是唯一的。
- `document_id` 应该是数据集中提供文档的ID。如果数据集中没有提供，可以将其设置为等于 top level `id`.
- `passages` 捕获文档结构，例如命名部分。如果没有文档结构，可以为空字段.
- `entities`,`events`,`coreferences`,`relations` 可能为空字段，具体取决于数据集和特定任务.



### 文本段落

段落捕获文档结构，例如文档的标题和摘要部分。 `Passages`如果没有文档结构，可以为空字段. 
- `offsets` 包含`" ".join([passage["text"] for passage in passages])`所创建的字符串中的字符偏移量.
- `offsets` and `text` 始终是支持不连续spans的列表. 对于连续跨度，它们将具有形式`offsets=[(lo,hi)], text=["text span"]`. 对于不连续的跨度，它们将具有以下形式 `offsets=[(lo1,hi1), (lo2,hi2), ...], text=["text span 1", "text span 2", ...]`


```
{
    "id": "0",
    "document_id": "227508",
    "passages": [
        {
            "id": "0",
            "type": "title",
            "text": ["Naloxone reverses the antihypertensive effect of clonidine."],
            "offsets": [[0, 59]]
        },
        {
            "id": "1",
            "type": "abstract",
            "text": ["In unanesthetized, spontaneously hypertensive rats the decrease in blood pressure and heart rate produced by intravenous clonidine, 5 to 20 micrograms/kg, was inhibited or reversed by nalozone, 0.2 to 2 mg/kg. The hypotensive effect of 100 mg/kg alpha-methyldopa was also partially reversed by naloxone. Naloxone alone did not affect either blood pressure or heart rate. In brain membranes from spontaneously hypertensive rats clonidine, 10(-8) to 10(-5) M, did not influence stereoselective binding of [3H]-naloxone (8 nM), and naloxone, 10(-8) to 10(-4) M, did not influence clonidine-suppressible binding of [3H]-dihydroergocryptine (1 nM). These findings indicate that in spontaneously hypertensive rats the effects of central alpha-adrenoceptor stimulation involve activation of opiate receptors. As naloxone and clonidine do not appear to interact with the same receptor site, the observed functional antagonism suggests the release of an endogenous opiate by clonidine or alpha-methyldopa and the possible role of the opiate in the central control of sympathetic tone."],
            "offsets": [[60, 1075]]
        },
    ],
}
```

### 实体（NER/NEN）
- `normalized` 子部分可以包含1个或多个规范化链接到数据库实体标识符。这里，“db_name”表示数据库名称，“db_id”表示该数据库中的实体标识符。

```
"entities": [
    {
        "id": "0",  
        "offsets": [[0, 8]],
        "text": ["Naloxone"],
        "type": "Chemical",
        "normalized": [{"db_name": "MESH", "db_id": "D009270"}]
    },
    ...
 ],
```


### 关系（RE）
- `type` 是关系类型. 
- `arg1_id` 是关系的第一个实体标识符. 
- `arg2_id` 是关系的第二个实体标识符. 

```
"relations": [
    {
        "id": "0",
        "type": "chemical-induced disease",
        "arg1_id": "10",
        "arg2_id": "32"
    }
]
```

### 因果关系（CRE）
- `type` 是关系类型. 
- `arg1` 是关系的第一个实体标识符。它可以是一个实体（arg 1 "type"应设置为 "entity"）或关系（arg2 "type"应设置为 "relation").
- `arg2` 是关系的第二个实体标识符。它可以是一个实体（arg 1 "type"应设置为 "entity"）或关系（arg2 "type"应设置为 "relation").

```
"causal": [
    {
        "id": "0",
        "type": "条件关系",
        "arg1": {"id":"3", "type":"entity"},
        "arg2": {"id":"0", "type":"relation"}
    }
]
```

### 事件（EE）

```
"events": [
    {
        "id": "0",
        "type": "Reaction",
        "trigger": {
            "offsets": [[0,6]],
            "text": ["reacts"]
        },
        "arguments": [
            {
                "role": "Theme",
                "ref_id": "5",
                "text": "corpus luteum"
            },
            {
                "role": "Instrument", # if the argument is not entity, set "ref_id" to "", only provide the text.
                "ref_id": ""
                "text": "...."
            }
        ]
    }
]

```

### 指代消解（COREF）
- `entity_ids` 表示多个实体名称引用同一实体.
```
"coreferences": [
	{
	   "id": "0",
	   "entity_ids": ["1", "10", "23"],
	},
	...
]
```

## 文本分类（Text Classification，TC）
这是一种简单的容器格式，具有最少的嵌套，支持一系列文本分类任务. (**比如: Chinese/TCM-SD-TC**)

```
{
    "id": "ABCDEFG",
    "document_id": "XXXXXX",
    "text": "xxxxx",
    "labels": [...]
}
```
**格式说明**

- `labels`是文本类型的标签.



例子:
```
{
    "id": "0",
    "document_id": "32653511",
    "text": "Potential benefits and risks of omega-3 fatty acids supplementation to patients with COVID-19.",
    "labels": ["Treatment"],
}
```

## 问答（Question Answering，QA）

这是一种简单的容器格式，具有最少的嵌套，支持一系列问答任务. 


```
{
    "id": "ABCDEFG",
    "document_id": "XXXXXX",
    "question_id": "xxxxx"
    "question": "...",
    "type": "...",
    "choices": [...],
    "context": "...",
    "answer": [...],
    "long_answer": [...]
}
```

**格式说明**

- `id` 字段出现在顶部（即文档）级别。它们以 "0" 开头，这使得数据集中的每个`id`字段都是唯一的.
- `document_id` 应该是数据集中提供文档的ID. 如果数据集中没有提供，可以将其设置为等于top level `id`.
- `question_id` 应该是数据集中提供问题的ID。如果数据集中没有提供，可以设置为等于上层 `document_id`.
- `question` 应该是问题输入。某些数据集的问题和上下文可能是独立的，请将上下文放入`context`字段中.
- `type` 可以是 "yesno", "multiple_choice" or "dialogue".
- `choices` 将被提供当数据类型是 "yesno" 或 "multiple_choice".
- `answer` 应该是答案输出. 一些 "yesno" and "multiple_choice". 数据集可能会提供额外的`long_answer`来解释选择,请将它们放入`long_answer`字段.
- `context`, `long_answer` 可能为空字段，具体取决于数据集和特定任务.






### 多项选择（Multiple Choice， multiple_choice）
(**示例文件: English/med_qa**)
```
{
    "id": "0",
    "question_id": "0",
    "document_id": "0",
    "question": "A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus. Which of the following is the best treatment for this patient?",
    "type": "multiple_choice",
    "choices": ["Ampicillin", "Ceftriaxone", "Ciprofloxacin", "Doxycycline", "Nitrofurantoin"],
    "context": "",
    "answer": ["Nitrofurantoin"],
    "long_answer": []
}
```
### 简单问答（Simple Answer Questions，sqa）
(**示例文件: Chinese/BenTsao_livercacer**)
```
{
    "id": "2",
    "question_id": "2",
    "document_id": "2",
    "question": "Hello doctor,I just got one side of my wisdom teeth removed both upper and lower six days ago, and I have another one scheduled after two days for the left side. The upper is 100 % fine, which they pulled. The lower they pulled the tooth without removing the root because it was too close to the nerve. I do have some stitching in this area currently on the lower cheek. Noticed a hard lump about 1 inch between my lower jawline and cheek area. Is this normal because of swelling or something else. Currently taking Amoxicillin 500 mg and Ibuprofen 600 mg. Please let me know what this hard lump is, also generally on the lower side where this lump is, remains sore.",
    "type": "sqa",
    "choices": [],
    "context": "",
    "answer": ["Hello. The lump is mostly a hard swelling which forms postsurgical removal of the wisdom tooth or maybe even by swollen lymph nodes due to infection. It takes a week or two for the swelling to subside. Sometimes, if the root is still inside, the infection may be remaining there causing swelling. Get an X-ray done to find out the exact problem and stronger antibiotics like Augmentin (Amoxicillin and Clavulanic acid) along with a painkiller for a week."],
    "long_answer": []
    }
```

### 基于上下文问答（Context-based Answer Questions，cqa）
(**示例文件: Chinese/TCM_Literature_QA**)

```
{
    "id": "0",
    "document_id": "828",
    "question_id": "0",
    "question": "“干呕、吐涎沫、头痛者吴茱萸汤主之”这句话曾出现在哪本医学巨著中？",
    "type": "cqa",
    "choices": [],
    "context": "反佐配伍的典范，始见于张仲景《伤寒杂病论》，其中记载“干呕、吐涎沫、头痛者吴茱萸汤主之”。患者病机为肝寒犯胃，浊气上逆所致头痛。胃阳不布产生涎沫随浊气上逆而吐出，肝脉与督脉交会于巅顶，肝经寒邪，循经上冲则头痛，以吴茱萸汤主治。可在吴茱萸汤中加入少许黄连反佐，用以防止方中吴茱萸、人参、干姜等品辛热太过，从而达到温降肝胃、泄浊通阳而止头痛的功效。后代医者多在清热剂和温里剂中运用此法。",
    "answer": "《伤寒杂病论》",
    "long_answer": []
}
```

## 多轮对话（Multi-Round Dialogue，MRD）
这是一种简单的容器格式，具有最少的嵌套，支持一系列多轮对话任务. (**示例文件: Chinese/MedDialog**)
```
{
    "id": "ABCDEFG",
    "conversation_id": "XXXXXX",
    "num_turns": int,
    "context": "...",
    "chat": [...],
}
```

**格式说明**

- `id` 段出现在顶部（即文档）级别。它们以 "0"开头,这使得数据集中的每个`id`字段都是唯一的.
- `conversation_id` 应该是数据集中提供的对话ID。如果数据集中没有提供，可以将其设置为等于top level `id`.
- `num_turns` 是聊天的总轮数.
- `chat` 应该是每轮的聊天上下文.
- `context` 根据数据集和特定任务，可能为空字段.

```
{
    "id": "159",
    "conversation_id": "159",
    "num_turns": 2,
    "context": "",
    "chat": [
        {
            "patient": "hello doctor, i get a cough for the last few days, which is heavy during night times. no raise in temperature but feeling tired with no travel history. no contact with any covid-19 persons. it has been four to five days and has drunk a lot of benadryl and took paracetamol too. doctors have shut the op so do not know what to do? please help.",
            "doctor": "hello, i understand your concern. i just have a few more questions. does your cough has phlegm? any other symptoms like difficulty breathing? any other medical condition such as asthma, hypertension? are you a smoker? alcoholic beverage drinker?"
        },
        {
            "patient": "thank you doctor, i have phlegm but not a lot. a tiny amount comes out most of the time. i have no difficulty in breathing. no medical conditions and not a smoker nor a drinker.",
            "doctor": "hi, i would recommend you take n-acetylcysteine 200 mg powder dissolved in water three times a day. you may also nebulize using pnss (saline nebulizer) three times a day. this will help the phlegm to come out. i would also recommend you take vitamin c 500 mg and zinc to boost your immune system. if symptoms persist, worsen or new onset of symptoms has been noted, further consult is advised."
        }
    ]
}
```

## 机器翻译（Machine Translation，MT）
这是一种简单的容器格式，具有最少的嵌套，支持一系列机器翻译任务. (**示例文件: English/paramed**)
```
{
    "id": "ABCDEFG",
    "document_id": "XXXXXX",
    "multilingual": [...]
}
```



**格式说明**

- `multilingual` 子组件可以包含两个或更多个规范化的并行文本.
- `language` 是本文的语言. "zh" 表示中文, "en" 表示英文.


```
{
	"id": "0",
	"document_id": "0",
	"multilingual": [
        {
            "id": "0",  
            "text": "也许不能: 分析结果提示激素疗法在维持去脂体重方面作用很小。",
            "language": "zh",
        },
        {
            "id": "1",  
            "text": "probably not: analysis suggests minimal effect of HT in maintaining lean body mass.",
            "language": "en",
        }
    ]
}
```




## 文本对（Text Pairs，TP）

这是一种简单的容器格式，具有最少的嵌套，支持一系列文本对任务


```
{
    "id": "ABCDEFG",
    "document_id": "XXXXXX",
    "text_1": "...",
    "text_2": "...",
    "label": [...]
}
```

**格式说明**

- `id` 字段出现在顶部（即文档）级别。它们以“0”开头，这使得数据集中的每个`id`字段都是唯一的.
- `document_id` 应该是数据集中提供的文档ID。如果数据集中没有提供，可以将其设置为等于 top level `id`.
- `text_1` 是第一个文本.
- `text_2` 是第二个文本.
- `label` 是文本对的标签.



### 文本蕴含（Textual Entailment，te）

```
{
	"id": "0",
	"document_id": "0",
	"text_1": "Pluto rotates once on its axis every 6.39 Earth days;",
	"text_2": "Earth rotates on its axis once times in one day.",
	"label": "neutral"
}
```
**格式说明**

- `text_1` 是前提.
- `text_2` 是假设.

### 语义相似度计算（Semantic Similarity，ss）

```
{
  "id": "0",
  "document_id": "0",
  "text_1": "Am I over weight (192.9) for my age (39)?",
  "text_2": "I am a 39 y/o male currently weighing about 193 lbs. Do you think I am overweight?",
  "label": "1"
}
```

**格式说明**

- `label` 是文本之间语义相似度相同的标签. 

## 文本到文本/结构（Text to Text/Struct，TT）
这是一种简单的容器格式，具有最少的嵌套，支持一系列文本生成任务. 
- 文本摘要
- 文本到结构 


```
{
    "id": "ABCDEFG",
    "document_id": "XXXXXX",
    "type": "...",
    "input": "...",
    "output": [...],
}
```
- `type` 可以是 "txt2txt" 或 "txt2struct".
### 文本摘要（Document Summarization，ds）
```
{
  "id": "0",
  "document_id": "1-131188152",
  "type": "txt2txt",
  "input": "SUBJECT: who and where to get cetirizine - D\nMESSAGE: I need/want to know who manufscturs Cetirizine. My Walmart is looking for a new supply and are not getting the recent",
  "output": ["Who manufactures cetirizine?"],
}
```
**格式说明**

- `input` 是原文.
- `output` 是摘要.

### 文本到结构（Text to Struct，ts）
```
{
  "id": "0",
  "document_id": "10301581",
  "type": "txt2struct",
  "input": "医生:你好，咳嗽是连声咳吗？有痰吗？有没流鼻涕，鼻塞？\n医生: 咳嗽有几天了？\n患者: 有三天\n......",
  "output": [{
                "主诉": "晚上咳嗽，磨牙。",
                "现病史": "患儿夜间咳嗽三天，磨牙，大便干。未服用药物。",
                "辅助检查": "暂缺。",
                "既往史": "不详。",
                "诊断": "消化不良。",
                "建议": "小儿消积止咳口服液，益生菌，到医院化验血常规。"
            }],
}
```
**格式说明**

- `input` 是输入文本.
- `output` 是结构输出.





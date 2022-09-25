这个还是不要直接用了, 它使用了一种称为 MRC 的 ner 格式.

```json
{
"context": "因 此 要 想 减 少 因 并 发 症 造 成 的 不 良 后 果 ， 必 须 提 高 住 院 分 娩 率 ， 将 住 院 分 娩 率 的 高 低 作 为 衡 量 产 前 保 健 工 作 水 平 的 一 项 重 要 指 标 。",
"end_position": [],
"entity_label": "NS",
"impossible": true,
"qas_id": "0.1",
"query": "按照地理位置划分的国家,城市,乡镇,大洲",
"span_position": [],
"start_position": []
},
{
"context": "因 此 要 想 减 少 因 并 发 症 造 成 的 不 良 后 果 ， 必 须 提 高 住 院 分 娩 率 ， 将 住 院 分 娩 率 的 高 低 作 为 衡 量 产 前 保 健 工 作 水 平 的 一 项 重 要 指 标 。",
"end_position": [],
"entity_label": "NR",
"impossible": true,
"qas_id": "0.2",
"query": "人名和虚构的人物形象",
"span_position": [],
"start_position": []
},
{
"context": "因 此 要 想 减 少 因 并 发 症 造 成 的 不 良 后 果 ， 必 须 提 高 住 院 分 娩 率 ， 将 住 院 分 娩 率 的 高 低 作 为 衡 量 产 前 保 健 工 作 水 平 的 一 项 重 要 指 标 。",
"end_position": [],
"entity_label": "NT",
"impossible": true,
"qas_id": "0.3",
"query": "组织包括公司,政府党派,学校,政府,新闻机构",
"span_position": [],
"start_position": []
}
```

对于每行文本, 会根据总的标签数, 输出 N 倍的数据.

这个 `zh_msra` 数据集, 就只有 3 个标签.

主要还是看下 loss 目录里, dice_loss 和 focal_loss 的实现.

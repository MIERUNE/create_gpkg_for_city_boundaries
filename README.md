# create_city_feather

e-statの境界データから市区町村でマージされた地物のfeatherファイルなどを作成するスクリプト群

## usage

- とても時間がかかるのでご注意ください

```shell
% cd scripts/
% ./run.sh
```

- `./data/merge_city_boundary.feather`が生成されれば処理完了

## list of data to be created

- boundary.gpkg：都道府県・市区町村・町丁目単位でマージされた3つレイヤを含むgpkg
- merge_boundary.gpkg：町丁目に平面直角座標系をカラムを付与したレイヤと19の平面直角座標系番号をキーにしてポリゴンをマージしたレイヤを含むgpkg
- merge_city_boundary.gpkg：上記の町丁目レイヤを市区町村単位にマージし直したレイヤ
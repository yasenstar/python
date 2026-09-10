from io import BytesIO
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import urllib3
import requests
from io import BytesIO

# Suppress insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- 解决 Matplotlib 中文乱码问题 ---
plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "SimHei",
    "Arial Unicode MS",
]  # 优先使用微软雅黑或黑体
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
# ----------------------------------

# 1. 销售数据
data = {
    "province": ["山东省", "甘肃省", "广东省"],
    "sales": [200, 115, 350]
}
df = pd.DataFrame(data)

# 2. 在线加载中国省级GeoJSON（DataV，无需本地文件）
geojson_url = "https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json"
response = requests.get(geojson_url, verify=False)
gdf = gpd.read_file(BytesIO(response.content))

# 合并地理数据和销售数据，匹配省份名称
merged_gdf = gdf.merge(df, how="left", left_on="name", right_on="province")

# 3. 绘图
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# 底色：全部省份浅灰色
gdf.plot(ax=ax, color="#e0e0e0", edgecolor="white", linewidth=0.4)

# 填色图：根据sales数值上色
merged_gdf.plot(
    column="sales",
    ax=ax,
    cmap="OrRd",
    legend=True,
    missing_kwds={
        "color": "#e0e0e0",
        "edgecolor": "white",
        "label": "No Data"
    },
    legend_kwds={
        "label": "销售数量 (Sales Volume)",
        "orientation": "vertical",
        "shrink": 0.6
    }
)

# 4. 美化
ax.set_title("China Provincial Sales Map", fontsize=15, fontweight="bold")
ax.axis("off")

plt.tight_layout()
plt.savefig("china_sales_map.png", dpi=300, bbox_inches="tight")
plt.show()

# 🏠 Housing Price Prediction with Linear Regression

This project uses linear regression to predict house prices based on housing features from the Ames Housing dataset. It includes data cleaning, feature engineering, model training, and interpretation of results using scikit-learn and pandas.

---

## 📁 Project Structure
- `model_pipeline.pkl`: Trained model pipeline
- `feature_importance.png`: Visual of top features
- `notebooks/`: Jupyter notebooks for EDA and modeling
- `submission.csv`: Final Kaggle-ready predictions

---

## ⚙️ Workflow

1. **Data Preprocessing**
   - Handled missing values (dropped or imputed)
   - Engineered new features like `TotalSF`, `TotalBath`, `GarageAge`, etc.
   - Categorized features like `Neighborhood` and `Exterior1st` into tiers based on average sale price

2. **Feature Encoding**
   - Categorical variables were encoded using `OneHotEncoder`
   - Target variable: `SalePrice`

3. **Modeling**
   - Used `Pipeline` with `SimpleImputer`, `OneHotEncoder`, and `Ridge` regression
   - Performance evaluated using **Mean Absolute Error (MAE)**

---

## 📊 Results

### 🔝 Top 10 Most Influential Features

| Feature                    | Impact on Price (USD) |
|---------------------------|------------------------|
| Neighborhood_Tier_Low     | –12,383                |
| Neighborhood_Tier_Mid     | –9,156                 |
| Exterior2nd_Tier_Mid      | +3,607                 |
| Exterior1st_Tier_Premium  | +2,687                 |
| Exterior1st_Tier_High     | +886                   |
| Exterior2nd_Tier_Low      | +492                   |
| Exterior1st_Tier_Mid      | –2,530                 |
| Exterior1st_Tier_Low      | –1,042                 |
| Exterior2nd_Tier_Premium  | –2,003                 |
| Exterior2nd_Tier_High     | –2,096                 |

*Note: Coefficients represent the change in predicted price compared to the reference category.*

---

## 🧠 Insights

- **Neighborhood matters:** Being in a low-tier neighborhood can reduce house value by over **$12,000**.
- **Material quality impacts price:** Premium materials for exterior 1st or 2nd tier generally increase value, but not always. Some "high-tier" materials have a negative impact — possibly due to design preferences or cost of upkeep.
- **Model performance:**  
  - **Training MAE**: ~$13,047  
  - **Baseline MAE**: ~$53,961 (mean model)

---

## 📁 Submission

The model was used to predict housing prices on the cleaned test dataset, and results were formatted for Kaggle submission (`submission.csv`).

---

## 🧾 How to Run

1. Clone the repo
2. Install requirements:  
   ```bash
   pip install pandas scikit-learn matplotlib seaborn plotly

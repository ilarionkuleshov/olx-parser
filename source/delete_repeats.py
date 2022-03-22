import pandas


source_file = 'olx.xlsx'
result_file = 'olx_odessa.xlsx'

#source_file = 'doba.xlsx'
#result_file = 'doba_result.xlsx'

print(f"{source_file} --> {result_file}")

excel_data_df = pandas.read_excel(source_file, sheet_name='Sheet')
excel_data_df.drop_duplicates(subset=['ID объявления'], inplace=True)
excel_data_df.to_excel(result_file, sheet_name='Sheet', index=False)

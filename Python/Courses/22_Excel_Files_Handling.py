# ============================================== Informations ==============================================

# pip3 install openpyxl                                 # install the openpyxl library
# pip3 freeze                                           # show the stuffs installed 
# from openpyxl import Workbook, load_workbook
# wb = Workbook()                                       # create a new workbook object 
# wb.create_sheet("sheet_name")                         # create a new worksheet 
# wb = load_workbook("Excel_file_path")                 # load existing worksheet
# ws = wb.active                                        # get the active worksheet
# ws = wb["Sheet_name"]                                 # access a specific worksheet by its name
# wb["sheet_name"].title = "new_title"                  # change the title of worksheet
# print(wb.sheetnames)                                  # return a list contain all sheets name from the workbook
# wb.save("workbook_name")

# ============================================== Write data ==============================================

# ------------------ One cell ------------------------

# ws.cell(column=values, row=values, value=)                        # methode 1
# ws["cell_name"] = value                                           # methode 2

# ----------------------------------------------------

# ws.append([value1, value2, value3])                               # insert row (by default after the last row)
# ws.insert_rows(3)                                                 # insert empty row at position 3
# ws.insert_cols(3)                                                 # insert empty column at position 3
# ws.delete_rows(3)                                                 # delete the row at the position 3
# ws.delete_cols(3)                                                 # delete the column at the position 3
# ws.move_range("cell_name:cell_name", rows=value, cols=values)     # moving range of cells    

# ============================================== Read data ==============================================


# ------------------ One cell ------------------------

# cell = ws["cell_name"]
# print(cell.value)

# ------------------ Row ------------------------

# print(ws[row_num])

# ------------------ Column ------------------------

# print(ws["column_name"])


# ------------------ Values ------------------------ 

# cell_range = ws["cell_name":"cell_name"]
# for cell in cell_range[0]:
#     print(cell.value)

# ============================================== Merge & Unmerge cells ==============================================

# ws.merge_cells("cell_name:cell_name")                   # the merged cell take the name of the first cell
# ws["merged_cell_name"] = value                          # just merged cell take this value and the rest cells in this merged cell are none
# delete = False

# import csv
# from typing import Any
# from fastapi.param_functions import Depends
# from stock.services.accounts import OperationsService

# from ..models.account import OperationCreate

# class ReportsService:
#     def __init__(self, operation_service: OperationsService = Depends()):
#         self.operations_service = operation_service

#     def import_csv(self, file: Any):
#         reader = csv.DictReader(
#             (line.decode() for line in file),
#             fieldnames=[
#                 'date',
#                 'kind',
#                 'amount',
#                 'description'
#             ],
#         )
#         operations = []
#         for row in reader:
#             operation_data = OperationCreate.parse_obj(row)
#             if operation_data.description == '':
#                 operation_data.description = None
#             operations.append(operation_data)

#         self.operations_service.create_many(
#             operations
#         )
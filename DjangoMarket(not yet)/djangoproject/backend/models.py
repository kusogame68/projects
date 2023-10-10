from django.db import models

# Create your models here.

class Customers(models.Model):
    id          = models.AutoField(primary_key=True,auto_created=True)
    first_name  = models.CharField(max_length=20)
    last_name   = models.CharField(max_length=20)
    account     = models.CharField(max_length=20)
    password    = models.CharField(max_length=20)
    born        = models.DateField()
    sex         = models.CharField(max_length=10)
    phone_number= models.CharField(max_length=10)
    email       = models.EmailField(max_length=50)
    country     = models.CharField(max_length=20)
    city        = models.CharField(max_length=20)
    address     = models.CharField(max_length=100)
    note        = models.TextField(max_length=100,null=True,blank=True)
    date_registered=models.DateField(auto_now_add=True)
    
class Employees(models.Model):
    id           = models.AutoField(primary_key=True,auto_created=True)
    first_name   = models.CharField(max_length=20)
    last_name    = models.CharField(max_length=20)
    account      = models.CharField(max_length=20)
    password     = models.CharField(max_length=20)
    # 學歷
    education    = models.CharField(max_length=50)
    # 部門
    department   = models.CharField(max_length=50)
    # 工作站
    position     = models.CharField(max_length=20)
    # 職等
    rank         = models.CharField(max_length=5)
    salary       = models.IntegerField()
    # 入職日
    hire_date    = models.DateField()
    # 是否在職
    is_active    = models.BooleanField(default=True)
    # 離職日
    termination_date = models.DateField(null=True, blank=True)
    born         = models.DateField()
    sex          = models.CharField(max_length=10)
    email        = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=10)
    country      = models.CharField(max_length=20)
    city         = models.CharField(max_length=20)
    address      = models.CharField(max_length=100)
    notes        = models.TextField(null=True,blank=True)

class Products(models.Model):
    id           = models.AutoField(primary_key=True,auto_created=True)
    product_name = models.CharField(max_length=100)
    category     = models.CharField(max_length=20)
    price        = models.IntegerField()
    quantity     = models.IntegerField()
    stock        = models.IntegerField()
    manufacturing_date = models.DateField()
    expiration_date = models.DateField()
    supplier     = models.CharField(max_length=20)
    manufacturing_location = models.CharField(max_length=20)
    brand        = models.CharField(max_length=20)
    date_added   = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now_add=True)
    
class Bill(models.Model):
    id           = models.AutoField(primary_key=True,auto_created=True)
    retail_name  = models.CharField(max_length=20,default='Johnson Retail')
    bill_number  = models.CharField(max_length=10)
    coutomers    = models.CharField(max_length=20)
    order_date   = models.DateField(auto_now_add=True)
    transaction_date = models.DateField(auto_now_add=True)
    payment_type = models.CharField(max_length=20)
    item_details = models.JSONField()
    total_amount = models.IntegerField()
    date_updated = models.DateField(auto_now_add=True)
    
    

    
'''
Customers：存储顾客信息，如customer_id：顾客唯一标识符，通常作为主键。
                            first_name：顾客的名字。
                            last_name：顾客的姓氏。
                            born ： 生日
                            sex：性別
                            email：顾客的电子邮件地址。
                            phone_number：顾客的电话号码。
                            address：顾客的地址。
                            city：顾客所在城市。
                            ###state：顾客所在州或省份。
                            country：顾客所在国家。
                            postal_code：顾客的邮政编码。
                            date_registered：顾客注册日期。

Employees：存储员工信息，如emp_id：員工編號
                            first_name：顾客的名字。
                            last_name：顾客的姓氏。
                            Education：學歷
                            department：部門
                            manager：上級
                            Position：职位
                            rank：職級
                            salary：薪水
                            hire_date 入職日期
                            is_active：是否在职的标志（布尔值）。
                            termination_date 離職日期
                            emergency_contact_name 緊急聯絡人
                            emergency_contact_phone 緊急聯絡人號碼
                            emergency_contact_relationship 緊急聯絡人關係
                            born ： 生日
                            sex：性別
                            email：电子邮件地址。
                            phone_number：电话号码。
                            address：地址。
                            city：所在城市。
                            state：所在州或省份。
                            country：顾客所在国家。
                            postal_code：顾客的邮政编码。
                            notes 備註



Products：存储产品信息，如产品ID (product_id)
                        名称 (name)
                        类别 (category)
                        价格 (price)
                        数量 (quantity)
                        製作日期 (manufacturing_date)
                        有效期限 (expiration_date)
                        产品描述 (product_description)
                        供应商 (supplier)
                        制造地点 (manufacturing_location)
                        品牌 (brand)
                        ###条形码 (barcode)
                        ###重量 (weight)
                        ###尺寸 (dimensions)
                        ###标签 (tags)
                        ###图片 (image)
                        ###特色产品 (featured)
                        ###是否可用 (is_available)
                        添加日期 (date_added)
                        更新日期 (date_updated)
                        

Orders：存储订单信息，如订单ID (order_id)
                        顾客ID (customer_id)
                        下单日期 (order_date)
                        总金额 (total_amount)
                        订单状态 (order_status)
                        支付方式 (payment_method)
                        支付状态 (payment_status)
                        配送地址 (shipping_address)
                        配送日期 (shipping_date)
                        配送状态 (shipping_status)
                        订单备注 (order_notes)
                        优惠码 (coupon_code)
                        创建日期 (date_created)
                        更新日期 (date_updated)


OrderItems：存储订单项信息，订单项ID (item_id)
                            订单ID (order_id)
                            产品ID (product_id)
                            数量 (quantity)
                            单价 (unit_price)
                            小计金额 (subtotal)
                            折扣金额 (discount_amount)
                            创建日期 (date_created)
                            更新日期 (date_updated)

Suppliers：存储供应商信息，如供应商ID (supplier_id)
                                名称 (name)
                                联系人姓名 (contact_person)
                                联系电话 (contact_phone)
                                联系邮箱 (contact_email)
                                地址 (address)
                                城市 (city)
                                州或省份 (state)
                                国家 (country)
                                邮政编码 (postal_code)
                                创建日期 (date_created)
                                更新日期 (date_updated)

Inventory：存储库存信息，跟踪每个产品的产品ID (product_id)
                                        供应商ID (supplier_id)
                                        库存数量 (stock_quantity)
                                        最低库存阈值 (min_stock_threshold)
                                        最高库存阈值 (max_stock_threshold)
                                        入库日期 (stock_in_date)
                                        出库日期 (stock_out_date)
                                        创建日期 (date_created)
                                        更新日期 (date_updated)

Sales：存储销售记录，记录每次销售的销售ID (sale_id)
                        订单ID (order_id)
                        销售日期 (sale_date)
                        销售金额 (sale_amount)
                        销售数量 (sale_quantity)
                        客户ID (customer_id)
                        创建日期 (date_created)
                        更新日期 (date_updated)

Discounts：存储折扣信息，如折扣ID (discount_id)
                        折扣类型 (discount_type)
                        折扣金额 (discount_amount)
                        开始日期 (start_date)
                        结束日期 (end_date)
                        创建日期 (date_created)
                        更新日期 (date_updated)

Transactions：存储交易ID (transaction_id)
                销售ID (sale_id)
                交易日期 (transaction_date)
                支付类型 (payment_type)
                交易金额 (transaction_amount)
                交易状态 (transaction_status)
                创建日期 (date_created)
                更新日期 (date_updated)
'''
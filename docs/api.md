# Restful HTTP API for Medical System

`https://localhost:5000[path][?query][#fragment]`

## 1. Doctor

### 1.1 全部医生

`/doctors`

### 1.2 筛选医生

`/doctors?q={query}&faculty={}&hospital={}&sortby={article,area}&order={asc,desc}&page={uint}`

### 1.3 单个医生

```
/doctors/:did
/doctors/:did/name
/doctors/:did/profession
/doctors/:did/political
/doctors/:did/expertise
/doctors/:did/description
/doctors/:did/status
/doctors/:did/hid
```

## 2. Hospital

### 2.1 全部医院

`/hospitals`

### 2.2 筛选医院

`/hospitals?q={query}&province={}&city={}&hosclass={}&sort={hosclass,area}&order={asc,desc}&page={uint}`

### 2.3 单个医院

```
/hospitals/:hid
/hospitals/:hid/hos_name
/hospitals/:hid/province
/hospitals/:hid/city
/hospitals/:hid/introduction
/hospitals/:hid/hos_class
/hospitals/:hid/address
```

## 3. Recommendation

### 3.1 Recommended Doctor

`/recommendation/doctors`

### 3.2 Recommended Hospital

`/recommendation/hospital`

## 4. Search



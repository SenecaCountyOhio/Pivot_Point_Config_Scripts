# Pivot Point Configuration Scripts

Pivot Point requires the following data:
- Parcels
- Permits(Full History)
- Permits(Work Orders)
- Sales


**When downloading a CSV from Inquire, you must reformat to standard *.csv.
*Inquire defaults to UTF-8 CSV which adds additional characters to the first
*field. Open the CSV in excel and click SAVE AS. Then select the type as CSV.**


## Parcels

1) Run "Pivot_Master_Parcel" shared query in Inquire and download as a csv.

2) Rename and save in the following directory;   

```
B:\\Projects\\Pivot Point\\Configuration_Scripts\\pre_config_data"
```

3) Open cmd and enter the following;

```
B:
```
```
cd B:\\Projects\\Pivot Point\\Configuration_Scripts"
```

4)  Enter "python Master_Parcels.py " and then the filename
that you saved in step 2. The following is an example;

```
python Master_Parcels.py master_parcels_12_03_2019.csv
```

A file is generated with the same name as the input in the following directory;

```
B:\\Projects\\Pivot Point\\Configuration_Scripts\\post_config_data
```

## Permits (Full History)

*Note: Permits (Full History) does not need to be reconfigured, just download as a csv from the saved query in inquire*

1) Run "Pivot_Point_Permit_FULL" shared query in Inquire and download as a csv.

## Permits (Word Order)

*Work Orders should be grouped by class (A/R & C/I)*

1) Run "Pivot_Point_Permit_COMM_IND" and "Pivot_Point_Permit_RES_AG" shared
queries in Inquire and download both as a csv.

2) Rename and save both in the following directory;
```
B:\\Projects\\Pivot Point\\Configuration_Scripts\\pre_config_data"
```

3) Open cmd and enter the following;

```
B:
```
```
cd B:\\Projects\\Pivot Point\\Configuration_Scripts"
```

4)  Enter "python Permits_WEEKLY.py " and then the filename
that you saved in step 2. The following is an example;

```
python Permits_WEEKLY.py permits_COMM_workorders.csv
```

A file is generated with the same name as the input in the following directory;

```
B:\\Projects\\Pivot Point\\Configuration_Scripts\\post_config_data
```

5) Repeat step 4 for the other file.

## Sales
*Note: Sales does not need to be reconfigured, just download as a csv from the
saved query in inquire*

1) Run "Pivot_Point_Sales_Export" shared query in Inquire and download as a csv.

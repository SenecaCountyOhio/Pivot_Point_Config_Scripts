# Pivot Point Configuration Scripts

Pivot Point requires the following data:
- Parcels
- Permits(Full History)
- Permits(Weekly)
- Sales

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

## Permits (Weekly)

## Sales
*Note: Sales does not need to be reconfigured in any way, just download as a csv from the saved query in inquire*

Run "Pivot_Point_Sales_Export" shared query in Inquire and download as a csv.

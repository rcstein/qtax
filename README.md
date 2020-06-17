# U.S. Census Bureau Quarterly State and Local Tax Data Summary

## Definitions

**Taxes** include all compulsory contributions, including penalty and interest receipts, collected for public purposes. This does not include unemployment and social insurance (e.g. social security, disability) taxes, nor does it include protested amounts, refunded amounts, or special assessments for public improvements. 

**Refunds** offset revenue for the year in which they were made, not the year of the tax to which they apply.  

**State government** includes agencies, institutions, commissions, and public authorities that operate completely or somewhat autonomously from the central state legislative, executive and judicial branches, but which are subject to state administrative or fiscal control over their activities. 

**Local or state** tax classification depends on which government is responsible for 2/3 of imposing, collecting, and retaining or distributing it. For example, a state-mandated tax which is levied and collected by a local government is credited to the local government. 

**Categories** are imposed by the Census Bureau and do not necessarily reflect how the states and localities categorize the taxes themselves. 

### Tax categories (after 2005): 

* Property taxes include general property taxes (e.g. land, cars), special taxes on certain types of property, and taxes based on income produced by property.

* Sales and gross receipts taxes are on goods and services based on volume or value of transfer, gross receipts or gross income from transfer, or an amount per unit sold. 

* Alcoholic beverages sales taxes are taxes on sale of alcoholic beverages, whether collected through government operated liquor stores or through private outlets. 

* Amusements sales taxes are taxes on admission tickets or admission charges and on gross receipts of all or specified types of amusement businesses. 

* Insurance premiums sales taxes are taxes imposed distinctively on insurance companies and measured by gross premiums or adjusted gross premiums.

* Motor fuels sales taxes include taxes on any fuel used in motor vehicles or aircrafts, and excludes taxes on the sale of fuel for any other purpose (e.g. heating). 

* Pari-mutuels sales taxes are taxes measured by betting or wagering amounts (e.g. horse-racing bets), including government collected “breakage”.

* Public utilities sales taxes are taxes imposed on public utilities, either as a direct tax on consumers or as a percentage of the utility’s gross receipts, and measured by gross receipts, gross earnings, or units of service sold. Includes passenger and freight transportation companies, telephone, telegraph, cable, and Internet service providers. 

* Tobacco products sales taxes are taxes on tobacco products, synthetic cigars and cigarettes, and related products like cigarette tubes and rolling papers. 

* Other selective sales and gross receipts taxes are taxes on specific commodities, businesses, or services not reported separately.  Includes sales or use taxes based on sales price, where the authorizing legislation is separate from the state’s general sales and use tax law. 

* Individual income taxes are taxes on individuals measured by net income and taxes on special types of income (e.g., interest, dividends, income from intangible property, etc.). For local governments, includes wages, salaries, and other compensation earned by both residents and nonresidents, that are subject to tax collections by the reporting government. Also includes combined individual and corporation income taxes where they could not be separated in historical data.

* Corporation Net Income Taxes are taxes on corporations and unincorporated businesses (when taxed separately from individual income), measured by net income, whether on corporations in general or on specific kinds of corporations, such as financial institutions. Includes “franchise” or “license” taxes where such taxes are calculated based on net income. 

* License taxes are those enacted as a condition to exercise a business or nonbusiness privilege, includes related fees and generally taxes on property levied on basis other than assessed value. 

* Death and gift taxes are taxes imposed on the transfer of property at death, in contemplation of death, or as a gift.

* Documentary and stock transfer taxes are taxes on the recording, registration, and transfer of documents.

* Severance taxes are taxes on the removal of natural resources from land or water by the quantity of products removed or sold. 


*The tax category definitions are largely unchanged from the system used prior to 2005. Consult the Census Bureau’s 1992 and 2006 Classification Manuals https://www.census.gov/topics/public-sector/about/classification-manual.html
for more detail.*


##  Data

Data is stored in the `Data` directory. 

`QTAX-mf.csv` is the full time series dataset available from the Census Bureau. Contains national totals, state level totals, and national and state level totals differentiated by tax category from 1992-2020Q1. Values are unadjusted in millions of dollars.

`QTAX-edit.csv` is contains unadjusted revenue by tax category and state from 1994-Q1 - 2020-Q1. This file was created by filtering and modifying (e.g. replacing coded index values for categories and states with their string names for ease of reference) `QTAX-mf.csv`.

Other csvs are individual time series for selected states and tax categories. The naming convention is state_category[_adj].csv. The suffix _adj denotes that a series has been seasonally adjusted with the `seasonal` package in R. 

Data before 1994 (state level) and 1992 (all other) is only available in PDF format, and has been excluded from analysis for the time being. 

## Methodology

**Population**: All 50 state governments and their respective local governments.

**Samples**: 
-    All 50 state governments
-    A stratified cluster sample of local tax collectors for local property taxes
-    Prior to 2010, a nonprobability sample of local tax imposers for local non-property taxes
-     After 2010, a stratified cluster sample of local tax imposers for local non-property taxes

**Collection**: Local government tax data responses are submitted via mail or web collection. State governments provide tax data via their central accounting systems. 

**Processing**: 
-    Data are received and processed from direct survey response forms and compilations of administrative and supplemental sources. 
-    Ratio edits of the current quarter’s value to the value in the same quarter of the prior year are used to identify possibly inaccurate data for correction or verification. 
-    Data from a variety of state organizational and accounting systems are re-classified to fit the Census Bureau’s uniform tax categories.

**Missing data handling**:
-    Local government property taxes are imputed* using a median growth rate multiplied by data from the same quarter in the prior year if such data is available. If prior year data is unavailable, missing data are imputed using the adjusted cell mean of the property tax amount. 

-    Local non-property taxes for the first quarter of 2012 were estimated with calibration** using 2007 Census of Governments Employment and Finance data. 
-    State government data are imputed using a national growth rate, after removing outliers, applied to the same quarter data from the prior year. 

-    Pro-rated statistics from external financial reports or the Census Bureau’s Annual Survey of State Government Finances and Annual Survey of State Tax Collections may be used to supplement state data when state reports are incomplete and all other data source investigations are exhausted.  

**Revision**:
-    Data may be revised for up to 7 quarters by the following methods:
o    Respondents submit revisions to originally reported amounts;
o    Respondents report previously unreported data that had been estimated;
o    Revisions are compiled from other published and unpublished government sources. 

**Error**:
-    State government data is not subject to sampling error because respondents comprise the complete population. However, inaccuracies in classification, coverage and processing are all possible sources of error.

-    Five state governments did not respond in the first quarter of 2012, so their data was imputed and thus subject to additional error. 

-    All local data is subject to sampling error. Property tax and post-2010 major non-property tax data are obtained from a probability sample designed to yield a national coefficient of variation under 3.0%. Pre-2010 non-property tax data are from a nonprobability sample, so the sampling error is unknown. 

**Imputation is the process of filling in missing or invalid data with reasonable values.*
**Calibration is the process of estimating the value of an independent variable from observed dependent variables when the statistical relationship is known (the reverse of regression).*

Sources: 
https://www.census.gov/programs-surveys/qtax/technical-documentation/methodology.html

U.S. Bureau of the Census Government Finance and Employment Classification Manual


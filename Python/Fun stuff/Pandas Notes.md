# **Pandas Notes**

### **Set_option**

```python
pd.set_option('display.max_columns', 10)
# Set the max number of columns displayed to be 10
pd.set_option('display.max_rows', 10)
# Set the max number of rows displayed to be 10
pd.set_option('display.width', 100)
# Set the display width to be 100
pd.set_option('display.float_format',lambda x: '%.5f'%x) 
# Set the precision of displayed values as 0.00001
```

### Shape

```python
df.shape
# df is a DataFrame, this would return a tuple (r,c)
# r is the row numbers and c is the column numbers
len(df)
# Return the number of rows in the dataset
df.columns
# Return the names of the columns
```

### Cut

```python
pd.cut(x, bins, right=True, labels=None, 
retbins=False, precision=3, include_lowest=False, duplicates='raise')
# Create categorical ranges for numerical data
```

- **x** is the value used to categorize

- **bins**: integer, list of scalars or separated indices
  
  1. If it's an integer, the data would be categorized into "bins" kind.
  
  2. If it's a list of scalars, the value would be the number used to decide the boundary. e.g. [1,2,3] the category would be (1,2),(2,3)
  
  3. If it's separated indices, indices should not overlap

- **right** is a boolean, if True, the right boundary would be inclusive. (1,2]

- **include_lowest** is a boolean, if True, the leftboundary would be inclusive. [1,2)

- **retbins** is a boolean to determine whether to show the boundary value for categorizing. (if bins is an integer, could be set to True)

- **labels**: array or boolean
  
  1. If it's an array, **len(labels)=bins**
  
  2. If it's a boolean, if False, return an integer describing the label of data.
  
  3. *Ignore this parameter if bins is separated indices.*

- **precision** is an integer to determine the precision for the categorizing label's value

- **duplicates** would trigger "Value Error" or elimininate non-unique value if the boundary for categorizing is not unique 

### Value_counts

The return type of this functio is **series**

```python
pd.value_counts(df,sort=True, ascending=False, 
normalize=False,bins=None,dropna=True)
# Return the counts of values in "df"
# if "normalize" is True, it would automatically perform normalization
# You could custom your intervals by changing "bins"
# if "dropna" is True, missing values would be dropped
```

### loc & iloc

```python
df.loc[]
df.iloc[]
```

loc is endpoint inclusive while iloc is endpoint-exclusive.

iloc requires you to enter the integer of the indices while loc requires you to enter the actual indicies.

e.g. df.loc["a","b"]  df.iloc[:2,1:3]

### Sort_values

```python
pd.sort_values(by=, axis=0, ascending=True, inplace=False, kind='quicksort', 
na_position='last')
```

- **axis**, axis = 0 'index', axis = 1 'columns'

- **by** here would be the values you want to sort, if axis = 0, it's a column name, if axis = 1, it's a row name

- **inplace** is a boolean indicating replace the original dataframe with the current sorted one or not

- **kind** would be the sorting algorithms including {'quicksort', 'mergesort', 'heapsort'}

- **na_position** includes {'first','last'}, indicating the position of the missing values

### unique & nunique

```python
df.unique()
# Return the unqiue value of the columns of "df" in the type of numpy.ndarray
df.nunqiue()
# Return the number of the unqiue value of the columns of "df"
```

### melt

```python
pd.melt(df, id_vars=None, value_vars=None, 
var_name=None, value_name='value', col_level=None)
# Convert some of the columns to rows
```

- id_vars: Names of the columns that **don't** need to be converted

- value_vars: Names of the columns that **need** to be converted

- var_name: customized name for the orginal column names

- value_name: customized name for the original value

- col_level: if columns is multiindex

### query

```python
df.query('(a>0) & (b<0)')
# Return the part of "df" that satisfies the condition
```

### isnull with any()

```python
df.isnull.any(axis=0)
# Check whether there is missing values in row
# If there is one True "any" would be True while "all" would be true if all True
```

### copy

```python
b = a.copy(deep=True)
# Return the deep copy, modification won't affect the original dataframe
```

### astype

Forced type conversion

```python
df = df.astype({'a':'int64','b':'float64'})
```

### groupby

```python
pd.groupby(by=None, axis=0, level=None, as_index=True, sort=True, dropna=True)
```

- **level**: If the axis is a MultiIndex (hierarchical), group by a particular level or levels. e.g. level = 0, level = 'type'

- **as_index**: For aggregated output, return object with group labels as the index.

- **sort**: boolean indicating sort group_keys or not

- **dropna**: If True, and if group keys contain NA values, NA values together with row/column will be dropped. If False, NA values will also be treated as the key in groups

Note that after groupby(), the return type would be DataFrameGroupBy, in order to convert back to DataFrame, we would apply a aggregate function.

e.g. df.groupby(by = "a").agg(['A':''mean','B':'count','C':func])

note that 'A','B','C' here would be column name after aggregation

#### Transform vs. agg vs. apply

- **transform could return a column vector while agg can't** since agg return a number e.g. df.groupby('order').transform(lambda x : x - np.mean(x))

- **apply** is more flexible! It could finish the job of both agg and transform.

### pivot_table

```python
pd.pivot_table(df, values=None, index=None, columns=None, aggfunc='mean', 
fill_value=None, margins=False, dropna=True, margins_name='All', sort=True)
```

- **values**: columns to aggregate

- **index**: list of columns or arrays

- **columns**: list of columns

- **aggfunc**: aggregating functions
  
  aggfunc could be a dict e.g. {'A':np.mean, 'B':np.max}

- **fill_value**: value to replace missing values

- **margins**: boolean indicating adding all row/columns or not

- **margins_name**: Name of the margins if margins is True

- **sort**: boolean indicating if the result should be sorted

### isna

```python
pd.isna(df)
# Check whether there are missing values or not
```

### isin

```python
pd.isin([list])
# Return a dataframe of booleans showing whether each element 
# in the DataFrame is contained in values.
```

### to_datetime

Useful when dealing with timestamps

```python
pd.to_datetime(arg,errors='raise', dayfirst=False, yearfirst=False, 
utc=None, format=None, unit=None, origin='unix')
```

- **errors**: {'ignore', 'raise', 'coerce'}, default 'raise'
  - If 'raise', then invalid parsing will raise an exception.
  - If 'coerce', then invalid parsing will be set as NaT.
  - If 'ignore', then invalid parsing will return the input.

- **dayfirst**: boolean indicating a date parse order

- **yearfirst**: boolean indicating a date parse order

  if yearfirst and dayfirst is both true, yearfirst is preceded

- **utc**: boolean indicating return utc DatetimeIndex or not

- **format**: The strftime to parse time
  e.g. “%d/%m/%Y”, note that “%f” will parse all the way up to nanoseconds

- **unit**: The unit of the arg (D,s,ms,us,ns), which is an integer or float number.

- **origin**: Define the reference date. 
  The numeric values would be parsed as number of units (defined by unit) since this reference date.
  - If ‘unix’ (or POSIX) time; origin is set to 1970-01-01.
  - If ‘julian’, unit must be ‘D’, and origin is set to beginning of Julian Calendar. 
    Julian day number 0 is assigned to the day starting at noon on January 1, 4713 BC.
  - If Timestamp convertible, origin is set to Timestamp identified by origin.

### merge

```python
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, 
left_index=False, right_index=False, sort=False, validate=None)
```

- **left**:DataFrame

- **right**: DataFrame or named Series,Object to merge with.

- **how**: Type of merge to be performed.
  
  - left: use only keys from left frame, similar to a SQL left outer join; preserve key order.
  
  - right: use only keys from right frame, similar to a SQL right outer join; preserve key order.
  
  - outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically.
  
  - inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys.
  
  - cross: creates the cartesian product from both frames, preserves the order of the left keys.

- **on**: label or list
  
  Column or index level names to join on. These must be found in both DataFrames. If on is None and not merging on indexes then this defaults to the intersection of the columns in both DataFrames.

- **left_on**: label or list, or array-like
  
  Column or index level names to join on in the left DataFrame. Can also be an array or list of arrays of the length of the left DataFrame. These arrays are treated as if they are columns.

- **right_on**: label or list, or array-like
  
  Column or index level names to join on in the right DataFrame. Can also be an array or list of arrays of the length of the right DataFrame. These arrays are treated as if they are columns.

- **left_index**: bool, default False
  
  Use the index from the left DataFrame as the join key(s). If it is a MultiIndex, the number of keys in the other DataFrame (either the index or a number of columns) must match the number of levels.

- **right_index**: bool, default False
  
  Use the index from the right DataFrame as the join key. Same caveats as left_index.

- **sort**: bool, default False
  
  Sort the join keys **lexicographically** in the result DataFrame. If False, the order of the join keys depends on the join type (how keyword).

- **validate**: str, optional
  
  If specified, checks if merge is of specified type.
  
  - “one_to_one” or “1:1”: check if merge keys are unique in both left and right datasets.
  
  - “one_to_many” or “1:m”: check if merge keys are unique in left dataset.
  
  - “many_to_one” or “m:1”: check if merge keys are unique in right dataset.
  
  - “many_to_many” or “m:m”: allowed, but does not result in checks.

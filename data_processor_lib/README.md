```mermaid
flowchart TB

Data[Data CSV]
Processor[Processor]
Descrip[Data Description]
Sum[Data Summary]
Charts[Charts / Graphs]
RcmdStgy[Recommended Strategy]

subgraph Conf[Configurations]
	%% Configurations goes here
end

subgraph Processor[Data Processor]
	%% Final result of the profiler

	Descrip
	-->Numerical

	Descrip
	--> Categorical

	Sum
	Charts
	RcmdStgy
end

Data --> Processor
Conf --> Processor

Processor --> Profile


```

## Questions:

- What we need inside data description, data summary and graphs, in order to help user identify what strategry is required for filling up the missing data.

## Data Processor Workflow

```mermaid
flowchart TB

initProcessor
----> ReadCsv
----> df
----> information

df
-----> dfModification
--modifiedDf----> df

df 
--> set_sample
--> sampleDf
--> sampleInformation

df 
--> impute

sampleDf
--> imputeSample

subgraph information
columns
head
overview
insights
extract_incompletes
end

subgraph dfModification[df_modification]
set_focus_columns
set_ignore_columns
set_ignore_rows
end

subgraph sampleInformation
sample_overview
sample_insights
end

subgraph imputeSample
end

subgraph impute
end

```

# Profiler Lib Documentation

#### Processor.set_focus(config)

**Parameters**:

- config: Either a list of available columns, or "\*" to select everything

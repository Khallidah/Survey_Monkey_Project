# Survey_Monkey_Project
import pandas as pd
import os
pwd=os.getcwd()
dataset=pd.read_excel("C:\\Users\idris\Documents\Data - Survey Monkey Output Edi.xlsx", sheet_name="Edited_Data")
dataset
Respondent.ID	Start.Date	End.Date	Email.Address	First.Name	Last.Name	Custom.Data.1	Identify.which.division.you.work.in....Response	Identify.which.division.you.work.in....Other.(please.specify)	Which.of.the.following.best.describes.your.position.level?...Response	...	Question.29...Response.8	Question.29...Response.9	Question.29...Response.10	Question.29...Response.11	Question.29...Response.12	Question.29...Response.13	Question.29...Response.14	Question.30...Response.1	Question.30...Response.2	Question.30...Response.3
0	5379192392	2021-01-22 12:01:17	2021-01-22 12:40:34	NaN	NaN	NaN	NaN	Infrastructure	NaN	Staff	...	NaN	Answer 8	Answer 8	Answer 4	NaN	NaN	Answer 5	NaN	NaN	NaN
1	2658722536	2021-01-22 06:56:37	2021-01-22 07:34:10	NaN	NaN	NaN	NaN	Finance	NaN	Staff	...	NaN	Answer 5	NaN	NaN	Answer 2	NaN	Answer 5	NaN	NaN	Answer 1
2	4044163394	2021-01-22 06:35:18	2021-01-22 06:47:32	NaN	NaN	NaN	NaN	Infrastructure	NaN	Department Lead	...	NaN	NaN	Answer 4	Answer 4	Answer 6	NaN	Answer 6	NaN	Answer 1	NaN
3	5535865599	2021-01-21 21:29:32	2021-01-21 21:40:24	NaN	NaN	NaN	NaN	Infrastructure	NaN	Manager	...	Answer 2	Answer 5	Answer 7	NaN	Answer 6	NaN	Answer 7	Answer 7	Answer 1	Answer 6
4	3356802928	2021-01-21 17:26:39	2021-01-21 17:44:40	NaN	NaN	NaN	NaN	Port Operations	NaN	Manager	...	NaN	Answer 5	Answer 4	Answer 4	Answer 7	Answer 7	NaN	Answer 7	NaN	Answer 8
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
193	7940065082	2021-01-11 06:19:18	2021-01-11 06:32:59	NaN	NaN	NaN	NaN	Infrastructure	NaN	Department Lead	...	Answer 1	Answer 1	Answer 3	Answer 6	Answer 6	Answer 8	NaN	NaN	NaN	Answer 8
194	5157705612	2021-01-11 06:19:14	2021-01-11 06:33:29	NaN	NaN	NaN	NaN	Finance	NaN	Staff	...	Answer 5	NaN	Answer 5	NaN	NaN	Answer 2	NaN	NaN	NaN	Answer 6
195	9920755555	2021-01-11 06:18:48	2021-01-11 06:27:27	NaN	NaN	NaN	NaN	Port Operations	NaN	Staff	...	NaN	Answer 7	NaN	NaN	NaN	NaN	NaN	NaN	Answer 3	NaN
196	6638341389	2021-01-11 06:19:01	2021-01-11 06:33:06	NaN	NaN	NaN	NaN	Infrastructure	NaN	Manager	...	Answer 2	NaN	Answer 3	Answer 5	NaN	Answer 8	Answer 3	Answer 3	NaN	NaN
197	8114622230	2021-01-11 06:18:50	2021-01-11 06:26:46	NaN	NaN	NaN	NaN	Information Technology	NaN	Staff	...	Answer 3	NaN	Answer 7	NaN	NaN	NaN	NaN	Answer 3	NaN	NaN
198 rows × 100 columns

dataset_modified=dataset.copy()
dataset_modified
Respondent.ID	Start.Date	End.Date	Email.Address	First.Name	Last.Name	Custom.Data.1	Identify.which.division.you.work.in....Response	Identify.which.division.you.work.in....Other.(please.specify)	Which.of.the.following.best.describes.your.position.level?...Response	...	Question.29...Response.8	Question.29...Response.9	Question.29...Response.10	Question.29...Response.11	Question.29...Response.12	Question.29...Response.13	Question.29...Response.14	Question.30...Response.1	Question.30...Response.2	Question.30...Response.3
0	5379192392	2021-01-22 12:01:17	2021-01-22 12:40:34	NaN	NaN	NaN	NaN	Infrastructure	NaN	Staff	...	NaN	Answer 8	Answer 8	Answer 4	NaN	NaN	Answer 5	NaN	NaN	NaN
1	2658722536	2021-01-22 06:56:37	2021-01-22 07:34:10	NaN	NaN	NaN	NaN	Finance	NaN	Staff	...	NaN	Answer 5	NaN	NaN	Answer 2	NaN	Answer 5	NaN	NaN	Answer 1
2	4044163394	2021-01-22 06:35:18	2021-01-22 06:47:32	NaN	NaN	NaN	NaN	Infrastructure	NaN	Department Lead	...	NaN	NaN	Answer 4	Answer 4	Answer 6	NaN	Answer 6	NaN	Answer 1	NaN
3	5535865599	2021-01-21 21:29:32	2021-01-21 21:40:24	NaN	NaN	NaN	NaN	Infrastructure	NaN	Manager	...	Answer 2	Answer 5	Answer 7	NaN	Answer 6	NaN	Answer 7	Answer 7	Answer 1	Answer 6
4	3356802928	2021-01-21 17:26:39	2021-01-21 17:44:40	NaN	NaN	NaN	NaN	Port Operations	NaN	Manager	...	NaN	Answer 5	Answer 4	Answer 4	Answer 7	Answer 7	NaN	Answer 7	NaN	Answer 8
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
193	7940065082	2021-01-11 06:19:18	2021-01-11 06:32:59	NaN	NaN	NaN	NaN	Infrastructure	NaN	Department Lead	...	Answer 1	Answer 1	Answer 3	Answer 6	Answer 6	Answer 8	NaN	NaN	NaN	Answer 8
194	5157705612	2021-01-11 06:19:14	2021-01-11 06:33:29	NaN	NaN	NaN	NaN	Finance	NaN	Staff	...	Answer 5	NaN	Answer 5	NaN	NaN	Answer 2	NaN	NaN	NaN	Answer 6
195	9920755555	2021-01-11 06:18:48	2021-01-11 06:27:27	NaN	NaN	NaN	NaN	Port Operations	NaN	Staff	...	NaN	Answer 7	NaN	NaN	NaN	NaN	NaN	NaN	Answer 3	NaN
196	6638341389	2021-01-11 06:19:01	2021-01-11 06:33:06	NaN	NaN	NaN	NaN	Infrastructure	NaN	Manager	...	Answer 2	NaN	Answer 3	Answer 5	NaN	Answer 8	Answer 3	Answer 3	NaN	NaN
197	8114622230	2021-01-11 06:18:50	2021-01-11 06:26:46	NaN	NaN	NaN	NaN	Information Technology	NaN	Staff	...	Answer 3	NaN	Answer 7	NaN	NaN	NaN	NaN	Answer 3	NaN	NaN
198 rows × 100 columns

columns_to_drop = ['Start.Date', 'End.Date', 'Email.Address', 'First.Name', 'Last.Name', 'Custom.Data.1']
columns_to_drop
['Start.Date',
 'End.Date',
 'Email.Address',
 'First.Name',
 'Last.Name',
 'Custom.Data.1']
dataset_modified = dataset_modified.drop(columns=columns_to_drop)
dataset_modified
Respondent.ID	Identify.which.division.you.work.in....Response	Identify.which.division.you.work.in....Other.(please.specify)	Which.of.the.following.best.describes.your.position.level?...Response	Which.generation.are.you.apart.of?...Response	Please.select.the.gender.in.which.you.identify....Response	Which.duration.range.best.aligns.with.your.tenure.at.your.company?...Response	Which.of.the.following.best.describes.your.employment.type?...Response	Question.1...Response	Question.2...Response	...	Question.29...Response.8	Question.29...Response.9	Question.29...Response.10	Question.29...Response.11	Question.29...Response.12	Question.29...Response.13	Question.29...Response.14	Question.30...Response.1	Question.30...Response.2	Question.30...Response.3
0	5379192392	Infrastructure	NaN	Staff	Generation X (born between 1965-1980)	Male	0-2 years	Full time Employee	NaN	Answer 6	...	NaN	Answer 8	Answer 8	Answer 4	NaN	NaN	Answer 5	NaN	NaN	NaN
1	2658722536	Finance	NaN	Staff	NaN	NaN	10+ years	Full time Employee	Answer 4	Answer 2	...	NaN	Answer 5	NaN	NaN	Answer 2	NaN	Answer 5	NaN	NaN	Answer 1
2	4044163394	Infrastructure	NaN	Department Lead	Generation X (born between 1965-1980)	Male	3-5 years	Full time Employee	Answer 5	Answer 7	...	NaN	NaN	Answer 4	Answer 4	Answer 6	NaN	Answer 6	NaN	Answer 1	NaN
3	5535865599	Infrastructure	NaN	Manager	Millennial (born between 1981-2000)	Non-Binary	5-10 years	Full time Employee	Answer 1	Answer 1	...	Answer 2	Answer 5	Answer 7	NaN	Answer 6	NaN	Answer 7	Answer 7	Answer 1	Answer 6
4	3356802928	Port Operations	NaN	Manager	Generation X (born between 1965-1980)	Female	10+ years	Full time Employee	NaN	Answer 3	...	NaN	Answer 5	Answer 4	Answer 4	Answer 7	Answer 7	NaN	Answer 7	NaN	Answer 8
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
193	7940065082	Infrastructure	NaN	Department Lead	Baby Boomer (born between 1946-1964)	Male	10+ years	Full time Employee	Answer 3	NaN	...	Answer 1	Answer 1	Answer 3	Answer 6	Answer 6	Answer 8	NaN	NaN	NaN	Answer 8
194	5157705612	Finance	NaN	Staff	Millennial (born between 1981-2000)	Female	5-10 years	Full time Employee	NaN	NaN	...	Answer 5	NaN	Answer 5	NaN	NaN	Answer 2	NaN	NaN	NaN	Answer 6
195	9920755555	Port Operations	NaN	Staff	Millennial (born between 1981-2000)	Female	3-5 years	Full time Employee	NaN	Answer 7	...	NaN	Answer 7	NaN	NaN	NaN	NaN	NaN	NaN	Answer 3	NaN
196	6638341389	Infrastructure	NaN	Manager	Millennial (born between 1981-2000)	Female	3-5 years	Full time Employee	NaN	NaN	...	Answer 2	NaN	Answer 3	Answer 5	NaN	Answer 8	Answer 3	Answer 3	NaN	NaN
197	8114622230	Information Technology	NaN	Staff	Prefer not to answer	Male	5-10 years	Full time Employee	NaN	Answer 1	...	Answer 3	NaN	Answer 7	NaN	NaN	NaN	NaN	Answer 3	NaN	NaN
198 rows × 94 columns

id_vars = list(dataset_modified.columns)[:8]
value_vars = list(dataset_modified.columns)[8: ]
dataset_melted = dataset_modified.melt(id_vars=id_vars, value_vars=value_vars, var_name="Question + Subquestion", value_name="Answers")
dataset_melted
Respondent.ID	Identify.which.division.you.work.in....Response	Identify.which.division.you.work.in....Other.(please.specify)	Which.of.the.following.best.describes.your.position.level?...Response	Which.generation.are.you.apart.of?...Response	Please.select.the.gender.in.which.you.identify....Response	Which.duration.range.best.aligns.with.your.tenure.at.your.company?...Response	Which.of.the.following.best.describes.your.employment.type?...Response	Question + Subquestion	Answers
0	5379192392	Infrastructure	NaN	Staff	Generation X (born between 1965-1980)	Male	0-2 years	Full time Employee	Question.1...Response	NaN
1	2658722536	Finance	NaN	Staff	NaN	NaN	10+ years	Full time Employee	Question.1...Response	Answer 4
2	4044163394	Infrastructure	NaN	Department Lead	Generation X (born between 1965-1980)	Male	3-5 years	Full time Employee	Question.1...Response	Answer 5
3	5535865599	Infrastructure	NaN	Manager	Millennial (born between 1981-2000)	Non-Binary	5-10 years	Full time Employee	Question.1...Response	Answer 1
4	3356802928	Port Operations	NaN	Manager	Generation X (born between 1965-1980)	Female	10+ years	Full time Employee	Question.1...Response	NaN
...	...	...	...	...	...	...	...	...	...	...
17023	7940065082	Infrastructure	NaN	Department Lead	Baby Boomer (born between 1946-1964)	Male	10+ years	Full time Employee	Question.30...Response.3	Answer 8
17024	5157705612	Finance	NaN	Staff	Millennial (born between 1981-2000)	Female	5-10 years	Full time Employee	Question.30...Response.3	Answer 6
17025	9920755555	Port Operations	NaN	Staff	Millennial (born between 1981-2000)	Female	3-5 years	Full time Employee	Question.30...Response.3	NaN
17026	6638341389	Infrastructure	NaN	Manager	Millennial (born between 1981-2000)	Female	3-5 years	Full time Employee	Question.30...Response.3	NaN
17027	8114622230	Information Technology	NaN	Staff	Prefer not to answer	Male	5-10 years	Full time Employee	Question.30...Response.3	NaN
17028 rows × 10 columns

questions_import = pd.read_excel("C:\\Users\idris\Documents\Data - Survey Monkey Output Edi.xlsx", sheet_name="Questions")
questions_import
Raw Questions	Sub Questions	Questions	Subquestions	Question + Subquestion
0	Respondent ID	NaN	Respondent ID	NaN	Respondent.ID
1	Start Date	NaN	Start Date	NaN	Start.Date
2	End Date	NaN	End Date	NaN	End.Date
3	Email Address	NaN	Email Address	NaN	Email.Address
4	First Name	NaN	First Name	NaN	First.Name
...	...	...	...	...	...
95	NaN	Response 13	Question 29	Response 13	Question.29...Response.13
96	NaN	Response 14	Question 29	Response 14	Question.29...Response.14
97	Question 30	Response 1	Question 30	Response 1	Question.30...Response.1
98	NaN	Response 2	Question 30	Response 2	Question.30...Response.2
99	NaN	Response 3	Question 30	Response 3	Question.30...Response.3
100 rows × 5 columns

questions = questions_import.copy()
questions.drop(columns=["Raw Questions", "Sub Questions", "Subquestions"], inplace=True)
questions
Questions	Question + Subquestion
0	Respondent ID	Respondent.ID
1	Start Date	Start.Date
2	End Date	End.Date
3	Email Address	Email.Address
4	First Name	First.Name
...	...	...
95	Question 29	Question.29...Response.13
96	Question 29	Question.29...Response.14
97	Question 30	Question.30...Response.1
98	Question 30	Question.30...Response.2
99	Question 30	Question.30...Response.3
100 rows × 2 columns

dataset_merged = pd.merge(left=dataset_melted, right=questions, how="left", left_on="Question + Subquestion", right_on="Question + Subquestion")
print("Original Data", len(dataset_merged))
print("Merged Data", len(dataset_merged))
Original Data 17028
Merged Data 17028
dataset_merged
Respondent.ID	Identify.which.division.you.work.in....Response	Identify.which.division.you.work.in....Other.(please.specify)	Which.of.the.following.best.describes.your.position.level?...Response	Which.generation.are.you.apart.of?...Response	Please.select.the.gender.in.which.you.identify....Response	Which.duration.range.best.aligns.with.your.tenure.at.your.company?...Response	Which.of.the.following.best.describes.your.employment.type?...Response	Question + Subquestion	Answers	Questions
0	5379192392	Infrastructure	NaN	Staff	Generation X (born between 1965-1980)	Male	0-2 years	Full time Employee	Question.1...Response	NaN	Question 1
1	2658722536	Finance	NaN	Staff	NaN	NaN	10+ years	Full time Employee	Question.1...Response	Answer 4	Question 1
2	4044163394	Infrastructure	NaN	Department Lead	Generation X (born between 1965-1980)	Male	3-5 years	Full time Employee	Question.1...Response	Answer 5	Question 1
3	5535865599	Infrastructure	NaN	Manager	Millennial (born between 1981-2000)	Non-Binary	5-10 years	Full time Employee	Question.1...Response	Answer 1	Question 1
4	3356802928	Port Operations	NaN	Manager	Generation X (born between 1965-1980)	Female	10+ years	Full time Employee	Question.1...Response	NaN	Question 1
...	...	...	...	...	...	...	...	...	...	...	...
17023	7940065082	Infrastructure	NaN	Department Lead	Baby Boomer (born between 1946-1964)	Male	10+ years	Full time Employee	Question.30...Response.3	Answer 8	Question 30
17024	5157705612	Finance	NaN	Staff	Millennial (born between 1981-2000)	Female	5-10 years	Full time Employee	Question.30...Response.3	Answer 6	Question 30
17025	9920755555	Port Operations	NaN	Staff	Millennial (born between 1981-2000)	Female	3-5 years	Full time Employee	Question.30...Response.3	NaN	Question 30
17026	6638341389	Infrastructure	NaN	Manager	Millennial (born between 1981-2000)	Female	3-5 years	Full time Employee	Question.30...Response.3	NaN	Question 30
17027	8114622230	Information Technology	NaN	Staff	Prefer not to answer	Male	5-10 years	Full time Employee	Question.30...Response.3	NaN	Question 30
17028 rows × 11 columns

respondents = dataset_merged[dataset_merged["Answers"].notna()]
respondents = respondents.groupby("Questions")["Respondent.ID"].nunique().reset_index()
respondents.rename(columns={"Respondent.ID":"Respondents"}, inplace=True)
respondents
Questions	Respondents
0	Question 1	119
1	Question 10	198
2	Question 11	164
3	Question 12	114
4	Question 13	108
5	Question 14	105
6	Question 15	114
7	Question 16	117
8	Question 17	135
9	Question 18	109
10	Question 19	157
11	Question 2	118
12	Question 20	105
13	Question 21	127
14	Question 22	160
15	Question 23	120
16	Question 24	195
17	Question 25	198
18	Question 26	193
19	Question 27	153
20	Question 28	119
21	Question 29	198
22	Question 3	117
23	Question 30	182
24	Question 4	161
25	Question 5	194
26	Question 6	196
27	Question 7	162
28	Question 8	190
29	Question 9	188
dataset_merged_two = pd.merge(left=dataset_merged, right=respondents, how="left", left_on="Questions", right_on="Questions")
print("Original Data", len(dataset_merged))
print("Merged Data", len(dataset_merged_two))
dataset_merged_two
Original Data 17028
Merged Data 17028
Respondent.ID	Identify.which.division.you.work.in....Response	Identify.which.division.you.work.in....Other.(please.specify)	Which.of.the.following.best.describes.your.position.level?...Response	Which.generation.are.you.apart.of?...Response	Please.select.the.gender.in.which.you.identify....Response	Which.duration.range.best.aligns.with.your.tenure.at.your.company?...Response	Which.of.the.following.best.describes.your.employment.type?...Response	Question + Subquestion	Answers	Questions	Respondents
0	5379192392	Infrastructure	NaN	Staff	Generation X (born between 1965-1980)	Male	0-2 years	Full time Employee	Question.1...Response	NaN	Question 1	119
1	2658722536	Finance	NaN	Staff	NaN	NaN	10+ years	Full time Employee	Question.1...Response	Answer 4	Question 1	119
2	4044163394	Infrastructure	NaN	Department Lead	Generation X (born between 1965-1980)	Male	3-5 years	Full time Employee	Question.1...Response	Answer 5	Question 1	119
3	5535865599	Infrastructure	NaN	Manager	Millennial (born between 1981-2000)	Non-Binary	5-10 years	Full time Employee	Question.1...Response	Answer 1	Question 1	119
4	3356802928	Port Operations	NaN	Manager	Generation X (born between 1965-1980)	Female	10+ years	Full time Employee	Question.1...Response	NaN	Question 1	119
...	...	...	...	...	...	...	...	...	...	...	...	...
17023	7940065082	Infrastructure	NaN	Department Lead	Baby Boomer (born between 1946-1964)	Male	10+ years	Full time Employee	Question.30...Response.3	Answer 8	Question 30	182
17024	5157705612	Finance	NaN	Staff	Millennial (born between 1981-2000)	Female	5-10 years	Full time Employee	Question.30...Response.3	Answer 6	Question 30	182
17025	9920755555	Port Operations	NaN	Staff	Millennial (born between 1981-2000)	Female	3-5 years	Full time Employee	Question.30...Response.3	NaN	Question 30	182
17026	6638341389	Infrastructure	NaN	Manager	Millennial (born between 1981-2000)	Female	3-5 years	Full time Employee	Question.30...Response.3	NaN	Question 30	182
17027	8114622230	Information Technology	NaN	Staff	Prefer not to answer	Male	5-10 years	Full time Employee	Question.30...Response.3	NaN	Question 30	182
17028 rows × 12 columns

same_answer = dataset_merged #  [dataset_merged["Answers"].notna()]
same_answer = same_answer.groupby(["Question + Subquestion", "Answers"])["Respondent.ID"].nunique().reset_index()
same_answer.rename(columns={"Respondent.ID":"Same Answer"}, inplace=True)
same_answer
Question + Subquestion	Answers	Same Answer
0	Question.1...Response	Answer 1	14
1	Question.1...Response	Answer 2	10
2	Question.1...Response	Answer 3	13
3	Question.1...Response	Answer 4	17
4	Question.1...Response	Answer 5	22
...	...	...	...
683	Question.9...Response.4	Answer 4	16
684	Question.9...Response.4	Answer 5	13
685	Question.9...Response.4	Answer 6	14
686	Question.9...Response.4	Answer 7	12
687	Question.9...Response.4	Answer 8	19
688 rows × 3 columns

dataset_merged_three = pd.merge(left=dataset_merged_two, right=same_answer, how="left", left_on=["Question + Subquestion", "Answers"], right_on=["Question + Subquestion", "Answers"])
dataset_merged_three["Same Answer"].fillna(0, inplace=True)
print("Original Data", len(dataset_merged_two))
print("Merged Data", len(dataset_merged_three))
dataset_merged_three
Original Data 17028
Merged Data 17028
Respondent.ID	Identify.which.division.you.work.in....Response	Identify.which.division.you.work.in....Other.(please.specify)	Which.of.the.following.best.describes.your.position.level?...Response	Which.generation.are.you.apart.of?...Response	Please.select.the.gender.in.which.you.identify....Response	Which.duration.range.best.aligns.with.your.tenure.at.your.company?...Response	Which.of.the.following.best.describes.your.employment.type?...Response	Question + Subquestion	Answers	Questions	Respondents	Same Answer
0	5379192392	Infrastructure	NaN	Staff	Generation X (born between 1965-1980)	Male	0-2 years	Full time Employee	Question.1...Response	NaN	Question 1	119	0.0
1	2658722536	Finance	NaN	Staff	NaN	NaN	10+ years	Full time Employee	Question.1...Response	Answer 4	Question 1	119	17.0
2	4044163394	Infrastructure	NaN	Department Lead	Generation X (born between 1965-1980)	Male	3-5 years	Full time Employee	Question.1...Response	Answer 5	Question 1	119	22.0
3	5535865599	Infrastructure	NaN	Manager	Millennial (born between 1981-2000)	Non-Binary	5-10 years	Full time Employee	Question.1...Response	Answer 1	Question 1	119	14.0
4	3356802928	Port Operations	NaN	Manager	Generation X (born between 1965-1980)	Female	10+ years	Full time Employee	Question.1...Response	NaN	Question 1	119	0.0
...	...	...	...	...	...	...	...	...	...	...	...	...	...
17023	7940065082	Infrastructure	NaN	Department Lead	Baby Boomer (born between 1946-1964)	Male	10+ years	Full time Employee	Question.30...Response.3	Answer 8	Question 30	182	14.0
17024	5157705612	Finance	NaN	Staff	Millennial (born between 1981-2000)	Female	5-10 years	Full time Employee	Question.30...Response.3	Answer 6	Question 30	182	20.0
17025	9920755555	Port Operations	NaN	Staff	Millennial (born between 1981-2000)	Female	3-5 years	Full time Employee	Question.30...Response.3	NaN	Question 30	182	0.0
17026	6638341389	Infrastructure	NaN	Manager	Millennial (born between 1981-2000)	Female	3-5 years	Full time Employee	Question.30...Response.3	NaN	Question 30	182	0.0
17027	8114622230	Information Technology	NaN	Staff	Prefer not to answer	Male	5-10 years	Full time Employee	Question.30...Response.3	NaN	Question 30	182	0.0
17028 rows × 13 columns

 output = dataset_merged_three.copy()
 output.rename(columns={"Identify.which.division.you.work.in....Response":"Division Primary", "Identify.which.division.you.work.in....Other.(please.specify)":"Division Secondary", 
    "Which.of.the.following.best.describes.your.position.level?...Response":"Position", "Which.generation.are.you.apart.of?...Response":"Generation", 
    "Please.select.the.gender.in.which.you.identify....Response":"Gender", "Which.duration.range.best.aligns.with.your.tenure.at.your.company?...Response":"Tenure", 
    "Which.of.the.following.best.describes.your.employment.type?...Response":"Employment"}, inplace=True)
output
Respondent.ID	Division Primary	Division Secondary	Position	Generation	Gender	Tenure	Employment	Question + Subquestion	Answers	Questions	Respondents	Same Answer
0	5379192392	Infrastructure	NaN	Staff	Generation X (born between 1965-1980)	Male	0-2 years	Full time Employee	Question.1...Response	NaN	Question 1	119	0.0
1	2658722536	Finance	NaN	Staff	NaN	NaN	10+ years	Full time Employee	Question.1...Response	Answer 4	Question 1	119	17.0
2	4044163394	Infrastructure	NaN	Department Lead	Generation X (born between 1965-1980)	Male	3-5 years	Full time Employee	Question.1...Response	Answer 5	Question 1	119	22.0
3	5535865599	Infrastructure	NaN	Manager	Millennial (born between 1981-2000)	Non-Binary	5-10 years	Full time Employee	Question.1...Response	Answer 1	Question 1	119	14.0
4	3356802928	Port Operations	NaN	Manager	Generation X (born between 1965-1980)	Female	10+ years	Full time Employee	Question.1...Response	NaN	Question 1	119	0.0
...	...	...	...	...	...	...	...	...	...	...	...	...	...
17023	7940065082	Infrastructure	NaN	Department Lead	Baby Boomer (born between 1946-1964)	Male	10+ years	Full time Employee	Question.30...Response.3	Answer 8	Question 30	182	14.0
17024	5157705612	Finance	NaN	Staff	Millennial (born between 1981-2000)	Female	5-10 years	Full time Employee	Question.30...Response.3	Answer 6	Question 30	182	20.0
17025	9920755555	Port Operations	NaN	Staff	Millennial (born between 1981-2000)	Female	3-5 years	Full time Employee	Question.30...Response.3	NaN	Question 30	182	0.0
17026	6638341389	Infrastructure	NaN	Manager	Millennial (born between 1981-2000)	Female	3-5 years	Full time Employee	Question.30...Response.3	NaN	Question 30	182	0.0
17027	8114622230	Information Technology	NaN	Staff	Prefer not to answer	Male	5-10 years	Full time Employee	Question.30...Response.3	NaN	Question 30	182	0.0
17028 rows × 13 columns

output_file_path = r"C:\Users\idris\OneDrive\Documents\Output Data.xlsx"
output.to_excel(output_file_path, index=False)
# DONE.

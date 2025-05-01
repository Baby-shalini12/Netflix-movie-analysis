{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "f84c2101-ecf2-4087-8fd2-779969689e95",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sb\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "0107a846-ab25-425d-a4a4-3bc6d626ed58",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Release_Date</th>\n",
       "      <th>Title</th>\n",
       "      <th>Overview</th>\n",
       "      <th>Popularity</th>\n",
       "      <th>Vote_Count</th>\n",
       "      <th>Vote_Average</th>\n",
       "      <th>Original_Language</th>\n",
       "      <th>Genre</th>\n",
       "      <th>Poster_Url\\r</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>15-12-2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>Peter Parker is unmasked and no longer able to...</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940</td>\n",
       "      <td>8.3</td>\n",
       "      <td>en</td>\n",
       "      <td>Action, Adventure, Science Fiction</td>\n",
       "      <td>https://image.tmdb.org/t/p/original/1g0dhYtq4i...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>01-03-2022</td>\n",
       "      <td>The Batman</td>\n",
       "      <td>In his second year of fighting crime, Batman u...</td>\n",
       "      <td>3827.658</td>\n",
       "      <td>1151</td>\n",
       "      <td>8.1</td>\n",
       "      <td>en</td>\n",
       "      <td>Crime, Mystery, Thriller</td>\n",
       "      <td>https://image.tmdb.org/t/p/original/74xTEgt7R3...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>25-02-2022</td>\n",
       "      <td>No Exit</td>\n",
       "      <td>Stranded at a rest stop in the mountains durin...</td>\n",
       "      <td>2618.087</td>\n",
       "      <td>122</td>\n",
       "      <td>6.3</td>\n",
       "      <td>en</td>\n",
       "      <td>Thriller</td>\n",
       "      <td>https://image.tmdb.org/t/p/original/vDHsLnOWKl...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>24-11-2021</td>\n",
       "      <td>Encanto</td>\n",
       "      <td>The tale of an extraordinary family, the Madri...</td>\n",
       "      <td>2402.201</td>\n",
       "      <td>5076</td>\n",
       "      <td>7.7</td>\n",
       "      <td>en</td>\n",
       "      <td>Animation, Comedy, Family, Fantasy</td>\n",
       "      <td>https://image.tmdb.org/t/p/original/4j0PNHkMr5...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>22-12-2021</td>\n",
       "      <td>The King's Man</td>\n",
       "      <td>As a collection of history's worst tyrants and...</td>\n",
       "      <td>1895.511</td>\n",
       "      <td>1793</td>\n",
       "      <td>7</td>\n",
       "      <td>en</td>\n",
       "      <td>Action, Adventure, Thriller, War</td>\n",
       "      <td>https://image.tmdb.org/t/p/original/aq4Pwv5Xeu...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Release_Date                    Title  \\\n",
       "0   15-12-2021  Spider-Man: No Way Home   \n",
       "1   01-03-2022               The Batman   \n",
       "2   25-02-2022                  No Exit   \n",
       "3   24-11-2021                  Encanto   \n",
       "4   22-12-2021           The King's Man   \n",
       "\n",
       "                                            Overview  Popularity Vote_Count  \\\n",
       "0  Peter Parker is unmasked and no longer able to...    5083.954       8940   \n",
       "1  In his second year of fighting crime, Batman u...    3827.658       1151   \n",
       "2  Stranded at a rest stop in the mountains durin...    2618.087        122   \n",
       "3  The tale of an extraordinary family, the Madri...    2402.201       5076   \n",
       "4  As a collection of history's worst tyrants and...    1895.511       1793   \n",
       "\n",
       "  Vote_Average Original_Language                               Genre  \\\n",
       "0          8.3                en  Action, Adventure, Science Fiction   \n",
       "1          8.1                en            Crime, Mystery, Thriller   \n",
       "2          6.3                en                            Thriller   \n",
       "3          7.7                en  Animation, Comedy, Family, Fantasy   \n",
       "4            7                en    Action, Adventure, Thriller, War   \n",
       "\n",
       "                                        Poster_Url\\r  \n",
       "0  https://image.tmdb.org/t/p/original/1g0dhYtq4i...  \n",
       "1  https://image.tmdb.org/t/p/original/74xTEgt7R3...  \n",
       "2  https://image.tmdb.org/t/p/original/vDHsLnOWKl...  \n",
       "3  https://image.tmdb.org/t/p/original/4j0PNHkMr5...  \n",
       "4  https://image.tmdb.org/t/p/original/aq4Pwv5Xeu...  "
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df= pd.read_csv(r\"C:\\Users\\HP\\Downloads\\Netflix.csv\",lineterminator = '\\n')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "47e9d345-2ac8-4c9c-a9bc-32a55ecd3456",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 9837 entries, 0 to 9836\n",
      "Data columns (total 9 columns):\n",
      " #   Column             Non-Null Count  Dtype  \n",
      "---  ------             --------------  -----  \n",
      " 0   Release_Date       9837 non-null   object \n",
      " 1   Title              9828 non-null   object \n",
      " 2   Overview           9828 non-null   object \n",
      " 3   Popularity         9827 non-null   float64\n",
      " 4   Vote_Count         9827 non-null   object \n",
      " 5   Vote_Average       9827 non-null   object \n",
      " 6   Original_Language  9827 non-null   object \n",
      " 7   Genre              9826 non-null   object \n",
      "        9837 non-null   object \n",
      "dtypes: float64(1), object(8)\n",
      "memory usage: 691.8+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "b39b1121-3545-424c-bec6-1886838eb97a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert Vote_Count and Vote_Average to numeric\n",
    "df['Vote_Count'] = pd.to_numeric(df['Vote_Count'], errors='coerce')\n",
    "df['Vote_Average'] = pd.to_numeric(df['Vote_Average'], errors='coerce')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "e23efb2d-4fc3-4dd6-acd7-2e9c17e0b1bc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    Action, Adventure, Science Fiction\n",
       "1              Crime, Mystery, Thriller\n",
       "2                              Thriller\n",
       "3    Animation, Comedy, Family, Fantasy\n",
       "4      Action, Adventure, Thriller, War\n",
       "Name: Genre, dtype: object"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Genre\"].head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "a1252037-bf36-4f91-beb7-ab7c3b465aeb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "b4d505d7-4797-4441-a408-32b1e3a7df3b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Popularity</th>\n",
       "      <th>Vote_Count</th>\n",
       "      <th>Vote_Average</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>9827.000000</td>\n",
       "      <td>9826.000000</td>\n",
       "      <td>9826.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>40.320570</td>\n",
       "      <td>1392.943721</td>\n",
       "      <td>6.439467</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>108.874308</td>\n",
       "      <td>2611.303856</td>\n",
       "      <td>1.129797</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>7.100000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>16.127500</td>\n",
       "      <td>146.000000</td>\n",
       "      <td>5.900000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>21.191000</td>\n",
       "      <td>444.000000</td>\n",
       "      <td>6.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>35.174500</td>\n",
       "      <td>1376.000000</td>\n",
       "      <td>7.100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>5083.954000</td>\n",
       "      <td>31077.000000</td>\n",
       "      <td>10.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Popularity    Vote_Count  Vote_Average\n",
       "count  9827.000000   9826.000000   9826.000000\n",
       "mean     40.320570   1392.943721      6.439467\n",
       "std     108.874308   2611.303856      1.129797\n",
       "min       7.100000      0.000000      0.000000\n",
       "25%      16.127500    146.000000      5.900000\n",
       "50%      21.191000    444.000000      6.500000\n",
       "75%      35.174500   1376.000000      7.100000\n",
       "max    5083.954000  31077.000000     10.000000"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "8d12c40d-3d7c-4ed6-b606-2aa5bdd4fc26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "datetime64[ns]\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HP\\AppData\\Local\\Temp\\ipykernel_7844\\1234164522.py:1: UserWarning: Parsing dates in %d-%m-%Y format when dayfirst=False (the default) was specified. Pass `dayfirst=True` or specify a format to silence this warning.\n",
      "  df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')\n"
     ]
    }
   ],
   "source": [
    "df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')\n",
    "print(df['Release_Date'].dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "3adffc48-6b48-4f19-89fe-0f15cf5ccf76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0      2021-12-15\n",
      "1      2022-03-01\n",
      "2      2022-02-25\n",
      "3      2021-11-24\n",
      "4      2021-12-22\n",
      "          ...    \n",
      "9832   1973-10-15\n",
      "9833   2020-10-01\n",
      "9834   2016-05-06\n",
      "9835   2021-03-31\n",
      "9836   1984-09-23\n",
      "Name: Release_Date, Length: 9837, dtype: datetime64[ns]\n"
     ]
    }
   ],
   "source": [
    "df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')\n",
    "print(df['Release_Date'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "612a89de-ad8e-4c11-a24c-0fbff7430b48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Release_Date'] = df['Release_Date'].dt.year\n",
    "df['Release_Date'].dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "522dd691-6057-4941-bef0-7f3f6acd184b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int32')"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Release_Date'] = df['Release_Date'].fillna(0).astype('int32')\n",
    "df['Release_Date'].dtypes\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "bbe73527-0fbe-4514-a052-8d57ac358fa3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Release_Date</th>\n",
       "      <th>Title</th>\n",
       "      <th>Overview</th>\n",
       "      <th>Popularity</th>\n",
       "      <th>Vote_Count</th>\n",
       "      <th>Vote_Average</th>\n",
       "      <th>Original_Language</th>\n",
       "      <th>Genre</th>\n",
       "      <th>Poster_Url\\r</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>Peter Parker is unmasked and no longer able to...</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>8.3</td>\n",
       "      <td>en</td>\n",
       "      <td>Action, Adventure, Science Fiction</td>\n",
       "      <td>https://image.tmdb.org/t/p/original/1g0dhYtq4i...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2022</td>\n",
       "      <td>The Batman</td>\n",
       "      <td>In his second year of fighting crime, Batman u...</td>\n",
       "      <td>3827.658</td>\n",
       "      <td>1151.0</td>\n",
       "      <td>8.1</td>\n",
       "      <td>en</td>\n",
       "      <td>Crime, Mystery, Thriller</td>\n",
       "      <td>https://image.tmdb.org/t/p/original/74xTEgt7R3...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2022</td>\n",
       "      <td>No Exit</td>\n",
       "      <td>Stranded at a rest stop in the mountains durin...</td>\n",
       "      <td>2618.087</td>\n",
       "      <td>122.0</td>\n",
       "      <td>6.3</td>\n",
       "      <td>en</td>\n",
       "      <td>Thriller</td>\n",
       "      <td>https://image.tmdb.org/t/p/original/vDHsLnOWKl...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021</td>\n",
       "      <td>Encanto</td>\n",
       "      <td>The tale of an extraordinary family, the Madri...</td>\n",
       "      <td>2402.201</td>\n",
       "      <td>5076.0</td>\n",
       "      <td>7.7</td>\n",
       "      <td>en</td>\n",
       "      <td>Animation, Comedy, Family, Fantasy</td>\n",
       "      <td>https://image.tmdb.org/t/p/original/4j0PNHkMr5...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021</td>\n",
       "      <td>The King's Man</td>\n",
       "      <td>As a collection of history's worst tyrants and...</td>\n",
       "      <td>1895.511</td>\n",
       "      <td>1793.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>en</td>\n",
       "      <td>Action, Adventure, Thriller, War</td>\n",
       "      <td>https://image.tmdb.org/t/p/original/aq4Pwv5Xeu...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Release_Date                    Title  \\\n",
       "0          2021  Spider-Man: No Way Home   \n",
       "1          2022               The Batman   \n",
       "2          2022                  No Exit   \n",
       "3          2021                  Encanto   \n",
       "4          2021           The King's Man   \n",
       "\n",
       "                                            Overview  Popularity  Vote_Count  \\\n",
       "0  Peter Parker is unmasked and no longer able to...    5083.954      8940.0   \n",
       "1  In his second year of fighting crime, Batman u...    3827.658      1151.0   \n",
       "2  Stranded at a rest stop in the mountains durin...    2618.087       122.0   \n",
       "3  The tale of an extraordinary family, the Madri...    2402.201      5076.0   \n",
       "4  As a collection of history's worst tyrants and...    1895.511      1793.0   \n",
       "\n",
       "   Vote_Average Original_Language                               Genre  \\\n",
       "0           8.3                en  Action, Adventure, Science Fiction   \n",
       "1           8.1                en            Crime, Mystery, Thriller   \n",
       "2           6.3                en                            Thriller   \n",
       "3           7.7                en  Animation, Comedy, Family, Fantasy   \n",
       "4           7.0                en    Action, Adventure, Thriller, War   \n",
       "\n",
       "                                        Poster_Url\\r  \n",
       "0  https://image.tmdb.org/t/p/original/1g0dhYtq4i...  \n",
       "1  https://image.tmdb.org/t/p/original/74xTEgt7R3...  \n",
       "2  https://image.tmdb.org/t/p/original/vDHsLnOWKl...  \n",
       "3  https://image.tmdb.org/t/p/original/4j0PNHkMr5...  \n",
       "4  https://image.tmdb.org/t/p/original/aq4Pwv5Xeu...  "
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "a1b8243e-7fca-49b9-bd55-f35f4c1e784f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Release_Date', 'Title', 'Overview', 'Popularity', 'Vote_Count', 'Vote_Average', 'Original_Language', 'Genre', 'Poster_Url\\r']\n"
     ]
    }
   ],
   "source": [
    "print(df.columns.tolist())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "b1e8c6ac-853e-4310-9400-61310549d8ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop(columns=['Overview', 'Original_Language', 'Poster_Url\\r'], errors='ignore', inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "075e33ca-a22b-416c-a4a7-461388df44f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Release_Date', 'Title', 'Popularity', 'Vote_Count', 'Vote_Average',\n",
       "       'Genre'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "e122a700-67a3-4dd9-b72e-1277d3d49490",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Release_Date</th>\n",
       "      <th>Title</th>\n",
       "      <th>Popularity</th>\n",
       "      <th>Vote_Count</th>\n",
       "      <th>Vote_Average</th>\n",
       "      <th>Genre</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>8.3</td>\n",
       "      <td>Action, Adventure, Science Fiction</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2022</td>\n",
       "      <td>The Batman</td>\n",
       "      <td>3827.658</td>\n",
       "      <td>1151.0</td>\n",
       "      <td>8.1</td>\n",
       "      <td>Crime, Mystery, Thriller</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2022</td>\n",
       "      <td>No Exit</td>\n",
       "      <td>2618.087</td>\n",
       "      <td>122.0</td>\n",
       "      <td>6.3</td>\n",
       "      <td>Thriller</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021</td>\n",
       "      <td>Encanto</td>\n",
       "      <td>2402.201</td>\n",
       "      <td>5076.0</td>\n",
       "      <td>7.7</td>\n",
       "      <td>Animation, Comedy, Family, Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021</td>\n",
       "      <td>The King's Man</td>\n",
       "      <td>1895.511</td>\n",
       "      <td>1793.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>Action, Adventure, Thriller, War</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Release_Date                    Title  Popularity  Vote_Count  \\\n",
       "0          2021  Spider-Man: No Way Home    5083.954      8940.0   \n",
       "1          2022               The Batman    3827.658      1151.0   \n",
       "2          2022                  No Exit    2618.087       122.0   \n",
       "3          2021                  Encanto    2402.201      5076.0   \n",
       "4          2021           The King's Man    1895.511      1793.0   \n",
       "\n",
       "   Vote_Average                               Genre  \n",
       "0           8.3  Action, Adventure, Science Fiction  \n",
       "1           8.1            Crime, Mystery, Thriller  \n",
       "2           6.3                            Thriller  \n",
       "3           7.7  Animation, Comedy, Family, Fantasy  \n",
       "4           7.0    Action, Adventure, Thriller, War  "
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "33f4683f-19fe-47a3-b9a1-46022ff502f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def categorise(df,col,labels):\n",
    "    edges = [df[col].describe()['min'],\n",
    "             df[col].describe()['25%'],\n",
    "             df[col].describe()['50%'],\n",
    "             df[col].describe()['75%'],\n",
    "             df[col].describe()['max']]\n",
    "    df[col]= pd.cut(df[col],edges, labels = labels, duplicates = 'drop')\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "48433887-05b8-4cd7-925d-c0bc7fb93f27",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['popular', 'below_average', 'average', 'not_popular', NaN]\n",
       "Categories (4, object): ['not_popular' < 'below_average' < 'average' < 'popular']"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "labels = ['not_popular', 'below_average', 'average', 'popular']\n",
    "categorise(df, 'Vote_Average', labels)\n",
    "df['Vote_Average'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "0b2e5c13-a278-42d2-b1a0-2bacb4acc972",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Release_Date</th>\n",
       "      <th>Title</th>\n",
       "      <th>Popularity</th>\n",
       "      <th>Vote_Count</th>\n",
       "      <th>Vote_Average</th>\n",
       "      <th>Genre</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Action, Adventure, Science Fiction</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2022</td>\n",
       "      <td>The Batman</td>\n",
       "      <td>3827.658</td>\n",
       "      <td>1151.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Crime, Mystery, Thriller</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2022</td>\n",
       "      <td>No Exit</td>\n",
       "      <td>2618.087</td>\n",
       "      <td>122.0</td>\n",
       "      <td>below_average</td>\n",
       "      <td>Thriller</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021</td>\n",
       "      <td>Encanto</td>\n",
       "      <td>2402.201</td>\n",
       "      <td>5076.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Animation, Comedy, Family, Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021</td>\n",
       "      <td>The King's Man</td>\n",
       "      <td>1895.511</td>\n",
       "      <td>1793.0</td>\n",
       "      <td>average</td>\n",
       "      <td>Action, Adventure, Thriller, War</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Release_Date                    Title  Popularity  Vote_Count  \\\n",
       "0          2021  Spider-Man: No Way Home    5083.954      8940.0   \n",
       "1          2022               The Batman    3827.658      1151.0   \n",
       "2          2022                  No Exit    2618.087       122.0   \n",
       "3          2021                  Encanto    2402.201      5076.0   \n",
       "4          2021           The King's Man    1895.511      1793.0   \n",
       "\n",
       "    Vote_Average                               Genre  \n",
       "0        popular  Action, Adventure, Science Fiction  \n",
       "1        popular            Crime, Mystery, Thriller  \n",
       "2  below_average                            Thriller  \n",
       "3        popular  Animation, Comedy, Family, Fantasy  \n",
       "4        average    Action, Adventure, Thriller, War  "
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "0ae9939c-6f6d-499a-b108-bb8d40af3632",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Release_Date    0\n",
       "Title           0\n",
       "Popularity      0\n",
       "Vote_Count      0\n",
       "Vote_Average    0\n",
       "Genre           0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dropna(inplace =True )\n",
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "be2b4255-435b-4808-bc94-05993f7cddf5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Release_Date</th>\n",
       "      <th>Title</th>\n",
       "      <th>Popularity</th>\n",
       "      <th>Vote_Count</th>\n",
       "      <th>Vote_Average</th>\n",
       "      <th>Genre</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Action, Adventure, Science Fiction</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2022</td>\n",
       "      <td>The Batman</td>\n",
       "      <td>3827.658</td>\n",
       "      <td>1151.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Crime, Mystery, Thriller</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2022</td>\n",
       "      <td>No Exit</td>\n",
       "      <td>2618.087</td>\n",
       "      <td>122.0</td>\n",
       "      <td>below_average</td>\n",
       "      <td>Thriller</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021</td>\n",
       "      <td>Encanto</td>\n",
       "      <td>2402.201</td>\n",
       "      <td>5076.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Animation, Comedy, Family, Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021</td>\n",
       "      <td>The King's Man</td>\n",
       "      <td>1895.511</td>\n",
       "      <td>1793.0</td>\n",
       "      <td>average</td>\n",
       "      <td>Action, Adventure, Thriller, War</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Release_Date                    Title  Popularity  Vote_Count  \\\n",
       "0          2021  Spider-Man: No Way Home    5083.954      8940.0   \n",
       "1          2022               The Batman    3827.658      1151.0   \n",
       "2          2022                  No Exit    2618.087       122.0   \n",
       "3          2021                  Encanto    2402.201      5076.0   \n",
       "4          2021           The King's Man    1895.511      1793.0   \n",
       "\n",
       "    Vote_Average                               Genre  \n",
       "0        popular  Action, Adventure, Science Fiction  \n",
       "1        popular            Crime, Mystery, Thriller  \n",
       "2  below_average                            Thriller  \n",
       "3        popular  Animation, Comedy, Family, Fantasy  \n",
       "4        average    Action, Adventure, Thriller, War  "
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "926aac23-1201-44d3-ae17-a1e59a3894a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Release_Date</th>\n",
       "      <th>Title</th>\n",
       "      <th>Popularity</th>\n",
       "      <th>Vote_Count</th>\n",
       "      <th>Vote_Average</th>\n",
       "      <th>Genre</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Action</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Adventure</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Science Fiction</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2022</td>\n",
       "      <td>The Batman</td>\n",
       "      <td>3827.658</td>\n",
       "      <td>1151.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Crime</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2022</td>\n",
       "      <td>The Batman</td>\n",
       "      <td>3827.658</td>\n",
       "      <td>1151.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Mystery</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Release_Date                    Title  Popularity  Vote_Count Vote_Average  \\\n",
       "0          2021  Spider-Man: No Way Home    5083.954      8940.0      popular   \n",
       "1          2021  Spider-Man: No Way Home    5083.954      8940.0      popular   \n",
       "2          2021  Spider-Man: No Way Home    5083.954      8940.0      popular   \n",
       "3          2022               The Batman    3827.658      1151.0      popular   \n",
       "4          2022               The Batman    3827.658      1151.0      popular   \n",
       "\n",
       "             Genre  \n",
       "0           Action  \n",
       "1        Adventure  \n",
       "2  Science Fiction  \n",
       "3            Crime  \n",
       "4          Mystery  "
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Genre'] = df['Genre'].str.split(', ')\n",
    "df = df.explode('Genre').reset_index(drop=True)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "eb15bafb-4b54-4bce-ac17-82f16ac97075",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "CategoricalDtype(categories=['Action', 'Adventure', 'Animation', 'Comedy', 'Crime',\n",
       "                  'Documentary', 'Drama', 'Family', 'Fantasy', 'History',\n",
       "                  'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction',\n",
       "                  'TV Movie', 'Thriller', 'War', 'Western'],\n",
       ", ordered=False, categories_dtype=object)"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Genre'] = df['Genre'].astype('category')\n",
    "df['Genre'].dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "94a7307c-b731-4b79-864b-624723dfc364",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 25551 entries, 0 to 25550\n",
      "Data columns (total 6 columns):\n",
      " #   Column        Non-Null Count  Dtype   \n",
      "---  ------        --------------  -----   \n",
      " 0   Release_Date  25551 non-null  int32   \n",
      " 1   Title         25551 non-null  object  \n",
      " 2   Popularity    25551 non-null  float64 \n",
      " 3   Vote_Count    25551 non-null  float64 \n",
      " 4   Vote_Average  25551 non-null  category\n",
      " 5   Genre         25551 non-null  category\n",
      "dtypes: category(2), float64(2), int32(1), object(1)\n",
      "memory usage: 749.6+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "806d2c4e-cfbe-42ce-862a-3c9a22d5fb8d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Release_Date     100\n",
       "Title           9414\n",
       "Popularity      8087\n",
       "Vote_Count      3265\n",
       "Vote_Average       4\n",
       "Genre             19\n",
       "dtype: int64"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "f4080cac-7503-4214-ae16-f936eced3b2b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Release_Date</th>\n",
       "      <th>Title</th>\n",
       "      <th>Popularity</th>\n",
       "      <th>Vote_Count</th>\n",
       "      <th>Vote_Average</th>\n",
       "      <th>Genre</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Action</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Adventure</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Science Fiction</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2022</td>\n",
       "      <td>The Batman</td>\n",
       "      <td>3827.658</td>\n",
       "      <td>1151.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Crime</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2022</td>\n",
       "      <td>The Batman</td>\n",
       "      <td>3827.658</td>\n",
       "      <td>1151.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Mystery</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Release_Date                    Title  Popularity  Vote_Count Vote_Average  \\\n",
       "0          2021  Spider-Man: No Way Home    5083.954      8940.0      popular   \n",
       "1          2021  Spider-Man: No Way Home    5083.954      8940.0      popular   \n",
       "2          2021  Spider-Man: No Way Home    5083.954      8940.0      popular   \n",
       "3          2022               The Batman    3827.658      1151.0      popular   \n",
       "4          2022               The Batman    3827.658      1151.0      popular   \n",
       "\n",
       "             Genre  \n",
       "0           Action  \n",
       "1        Adventure  \n",
       "2  Science Fiction  \n",
       "3            Crime  \n",
       "4          Mystery  "
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1721fc42-d3bb-48e4-8c7e-bb1907526389",
   "metadata": {},
   "source": [
    "  # Data Visualisation "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "78cdd93b-8343-4ee2-b8ce-60f0aa6120ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "sb.set_style('whitegrid')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dee5342a-9615-428f-8eec-cc63c607d126",
   "metadata": {},
   "source": [
    "What is the most frequent genre of movies related on Netflix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "a9d9d9da-0e85-411c-9b33-5640de9f7cbd",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HP\\Downloadsanaconda3\\Lib\\site-packages\\seaborn\\categorical.py:641: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.\n",
      "  grouped_vals = vals.groupby(grouper)\n",
      "C:\\Users\\HP\\Downloadsanaconda3\\Lib\\site-packages\\seaborn\\categorical.py:641: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.\n",
      "  grouped_vals = vals.groupby(grouper)\n"
     ]
    },
    {
     "data": {
      "image/png": "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+/XXXwE0jzI9KueLzL///qspS0tLIzExMV/XWhQWLVpEZmYmXbt21bn9s88+00wAtLGxoV27dgwYMICsrCzNl5ZHu66f1++//671e0REBCYmJprnsq2trbXuJ5Br4tuzzl+vXj0uXbrEsWPHtMp//fVXzM3NqVOnTn7DFy9IWtRCFACVSsXMmTMZOXIknTt35p133kGlUpGVlcWxY8fYuHEj165do0+fPpr9O3TowNixY7l06RJubm6a2byVK1fW2Qp+Hq+99hp9+vRh7ty5pKen4+Pjw5UrV5g7dy4mJibUqFHjicf6+/tz4MABJk+ezPHjx2nbti0lSpQgLi6OFStW8NprrzF58mQAmjZtio+PD2PGjOHKlSvUqFGDw4cPs3TpUt566y2dzwSrVCoqVqzIggULsLa21kyge7w7VR/+++8/YmNjgYct1OvXr7N9+3bCw8Pp16+fVg/Joxo0aMD48eOZMWMGTZs25datW8yfP58qVapo7nWpUqU4deoUhw8ffu6kd+LECUaPHk1gYCAnTpxg3rx5vPPOO5p/J2+++SaLFy9m8eLFuLu7s2vXLg4dOqRVR04vy44dO2jatGmuGeadO3dm7dq1DBw4kCFDhlC5cmV27drFzz//zKBBgzTHi6IniVqIAtKmTRvc3NxYt24dGzdu5NKlSyiKgoODA/7+/rz33ntaCXjatGksXryYH3/8kX///RdbW1v8/f357LPPco355sdnn32GnZ0da9eu5bvvvqN06dI0bNiQzz//XGsyli6TJ0/Gx8eH9evXM27cOO7cuUOlSpXo0qULvXv31nSD5iTZefPmsXLlSv777z8qV67M559/Ts+ePXXWbWpqyrx585g6dSqff/455cqV46OPPiIpKYnk5OQXvu4XsXfvXs3bu0xMTChVqhSurq7MmzePNm3aPPG49957j8zMTH788UfWrl2LpaUlDRs2ZNiwYZibmwPQq1cvpk6dSu/evVmxYsVzxTVw4EBOnjxJv379sLGxoU+fPgwaNEizvW/fvvz3338sW7aMzMxMmjdvzpQpU+jfv79mHx8fHxo1asSsWbM4ePAgS5Ys0TqHlZUVq1evZtasWZoveM7OzkyZMoV33nnnueIVBctEkTe0CyGEEAZLxqiFEEIIAyaJWgghhDBgkqiFEEIIAyaJWgghhDBgkqiFEEIIAyaJWggh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vP766+zfv5+KFSuyZs0atmzZwqxZs/jpp5+wtbWlV69eZGZmauLbvXs369at48svvwTg2LFjJCcns27dOsaOHcuqVas4cOBA0d40IYQQBUZmfeeBt7e3JlFHR0fj4+MDQP369QkPDwf+Nz69ZcsWbG1t+eyzzwCoUqUKly5dYtWqVXTq1IlLly5RsmRJKleujJWVFXPnzgUefiGwsbHB1NQUO7uHjzp99913jB8/XnO+iRMn4uvry759+/Dz8wOga9euODs7AxAXF4darWbSpElYW1vj7OzMypUrOXHiBI0bNy6amyWEEKJASaLOA29vb02LODo6mkmTJgEPE/X06dPJyMggNjaW/v37c/z4cU6fPo2np6fmeLVarXmByIcffsiAAQNo2LAhDRs2pE2bNrRv3z7XOe/cucO///7L0KFDKVbsfx0f9+/f59y5c5rf7e3ttY6ztbXF2tpa87u1tTVZWfKYlRBCGCtJ1Hng6enJ1atXOXHiBFevXqVu3boAVKtWDRsbG44cOcLZs2epX78+R48epWHDhowbN05nXQ0bNmTv3r3s3LmTPXv2MG7cOPbv388333yjtV/O6lVz587FyclJa1vp0qU1n4sXL661zcLCItc5ZYxaCCGMl4xR50GJEiWoWbMmP/30E7Vr18bKygoAExMT6tWrR1hYGFWqVKFs2bI4OTmRnJxM5cqVcXR0xNHRkdjYWFavXg3AypUriY+P56233mLu3LlMmzaNyMhITX05SpUqha2tLampqZp6KlasyMyZM0lOTi76myCEEEIvJFHnUb169YiIiMj1+FX9+vXZuXMn9erVA6BDhw7cv3+fcePGkZiYyN69e5kyZQq2trbAw1njEydOJDY2lnPnzrF9+3ZcXV0BsLKyIi0tjXPnzpGVlUWPHj0ICQlh165dnDt3jjFjxhATE6MZkxZCCPHyk67vPPLy8mL58uWaiV056tevz7179zQJ3NramqVLlzJ16lQ6depEmTJleP/99+nbty8An376Kbdv36Z///7cvXuXevXqMXPmTAAaNGiAo6Mj7du3Z+3atfTu3Zs7d+4wbtw40tPTcXNzY9myZVpd30IIIV5uJooMYIpHqNVqYmNjmTq1AjExeZuEVquWBeHhlQo5sifLidnDw+O5V/3SB2OLF4wvZmOLF4wvZom36EjXtxBCCGHApOtb6OTs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",
      "text/plain": [
       "<Figure size 500x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sb.catplot(y='Genre',data = df, kind = 'count', color = 'Blue',order = df['Genre'].value_counts().index)\n",
    "plt.title('Genre Column Distribution')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3ff50f2b-cc53-4e6b-8616-82886be6df62",
   "metadata": {},
   "source": [
    "2.Which has highest vote in vote avg Column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "5ae1793b-1f31-4437-af41-c71263fe72c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HP\\Downloadsanaconda3\\Lib\\site-packages\\seaborn\\categorical.py:641: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.\n",
      "  grouped_vals = vals.groupby(grouper)\n",
      "C:\\Users\\HP\\Downloadsanaconda3\\Lib\\site-packages\\seaborn\\categorical.py:641: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.\n",
      "  grouped_vals = vals.groupby(grouper)\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAeoAAAH+CAYAAABTKk23AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/TGe4hAAAACXBIWXMAAA9hAAAPYQGoP6dpAABCfklEQVR4nO3dd1yVdf/H8TfDTOVW3HeOlNLIwXbkVjIHAg6yFLWsXGlZaSmWUd3qbaWZqZW4R4MsFUelqLnSEhyghBNxoIWYWm7gcP3+8Pb8JDRBOZ0LeD0fDx6d873W53NhvM81zjkOhmEYAgAApuRo7wIAAMCtEdQAAJgYQQ0AgIkR1AAAmBhBDQCAiRHUAACYGEENAICJEdQAAJgYQQ0g1wrK5yOZoU4z1IDCgaAGCqFnnnlGjRo1Unp6+i3nCQoKUq9evXK1vj///FMjRozQ9u3b77q2Pn36yN3d3frz8MMPy8fHR926ddOCBQuUmZmZbX5/f3+FhYXlev3r1q3TyJEjbztfWFiY/P3973g7t3KzfdWnTx/16dPnrteNosnZ3gUAyH8hISHaunWrNm3apLZt2+aY/ssvv+jAgQN67733crW+vXv3atmyZQoJCcmX+urWrau33npLkmSxWPTHH39o06ZNGj9+vLZv367JkyfL0fHaccS0adPk4uKS63XPmzcvV/MNHjxYTz31VJ5rv52b7avrvQJ3gqAGCqHHHntMZcqU0fLly28a1EuXLpWLi4vat29vh+okFxcXeXt7Zxvz9/fXAw88oHHjxmnlypUKDg6WdC3UbeH++++3yXpvplatWv/YtlD4cOobKISKFy+uwMBAbdiwQRcuXMg2LSMjQ99++606deqkEiVKSJK2bNmi0NBQ+fn5qXHjxho+fLh+/fVXSdK2bdusR55PPfVUtlO4a9euVbdu3eTh4aFmzZpp7NixunTp0h3X3bt3b1WuXFmRkZHWsb+ekr4e4p6ennrkkUf06quvKjU1VdK1U8wxMTGKiYmRu7u7tm3bpm3btsnd3V2RkZFq06aNfH19tWXLlhynvq/vm7Fjx6phw4Zq0KCBRo4cqTNnzlin3+wU9vX1X9/WzfbVX5e7evWqPv74Y3Xo0EEeHh5q166dZsyYoaysrGzbeuONNzRjxgy1bt1aHh4e6tGjh3bv3n3H+xcFE0ENFFIhISG6evWqVq9enW1806ZNOnPmjLp37y5JioqK0rPPPqv77rtPkyZN0qhRo7Rr1y49+eST+v3331WvXj2Fh4dLksLDw62ncVesWKEhQ4bogQce0Mcff6wXXnhBy5cv1+DBg+/4RipHR0c1adJEu3fvznGtWpJ27NihESNGqF27dpo5c6ZGjRqln3/+WcOHD5d07RRz3bp1VbduXX311VeqV6+eddlp06Zp5MiRCg8Pl4+Pz023//333+uXX37Ru+++q5EjR2rDhg3q37+/LBZLruq/1b66kWEYGjRokGbNmqXu3btr+vTp6tChgyZPnpxj/tWrV2vdunUaPXq0Jk2apNOnT+vFF1/MdT0oHDj1DRRS9erVU506dbRixYps10ujoqLk7u4uDw8PZWVlaeLEiWrevLk++OAD6zy+vr4KCAjQ7NmzNWLECOup21q1aqlWrVoyDEMTJ05UixYtNHHiROtyNWvWVN++fbVx40a1bt36juquUKGCMjIydO7cOVWoUCHbtB07dujee+/VgAEDdM8990iSXF1dtWfPHhmGoVq1almvZ//11HpoaKg6dOjwt9suW7asZs+erZIlS1qfDxkyRJs2bVKbNm1uW7uLi0uOffVXmzZt0tatWzVp0iR16tRJktSsWTPde++9+uijj/TUU0+pdu3akqTMzEzNnj3b2tPFixc1cuRI7d27V/Xr179tPSgcOKIGCrGQkBBt27bNemr43LlzWr9+vR5//HFJUnJystLS0hQYGJhtufvvv18+Pj6KiYm56XoPHz6s3377Tf7+/srMzLT+NGzYUC4uLtqyZcsd13z9aNzBwSHHtIYNG+ry5csKDAzUBx98oO3bt6t58+Z64YUXbjr/jerUqXPbbbdq1coa0tK10+7Ozs6KjY3NYxe3FhMTI2dn5xwvGq5fk79xn9/4wkOSKleuLEm6fPlyvtUD8yOogUIsKChIzs7O+u677yRJ3377rRwcHKyhcO7cOUnKceR6fez8+fM3Xe/15d555x3Vq1cv28+FCxd06tSpO645NTVV9957r1xdXXNM8/Hx0YwZM1S9enXNnTtXvXr1UsuWLbVw4cLbrvfGAL6VihUrZnvu6OiosmXL6s8//8x1/bfzxx9/qGzZsnJycrrptm/c59fvIbixHknZrmWj8OPUN1CIubq6qm3btlqxYoWeeeYZLVu2TI899pg1BK//9/Tp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RJUrV9aAAQOUnp6ep20fO3ZML730kkJDQ/X9999r8uTJ2rp1qxYtWmSdZ926dQoMDNT8+fPl6emZb30DAGzP2d4FFAavvfaaGjRoIEl66aWXNHHiRB06dEjt27dX3759JUlubm7avXu35syZo0mTJkmSWrZsaZ0+ZswYtWjRQlu2bFHt2rVzve2srCyNHj1aTzzxhCSpWrVqatq0qQ4ePGidp0KFCurZs2c+dAoA+KcR1PnA19fX+rh+/fo6c+aMDh8+rB49emSbz8fHR4sXL77pci4uLnJzc1NSUlKegrpmzZq655579Omnn+rgwYM6ePCgDh06pM6dO1vnqVq16p20BQAwAU5954NixYpZH2dlZUmSrl69mmO+rKws63RJcnbO/jrJYrHI0dFRDg4OOZa9ft37r/bt26dOnTrp0KFDatCggcaNG6eAgIBs8xQvXjz3zQAATIUj6nywd+9eNWrUSJKUkJCgSpUqycvLS/Hx8dnm27Vrl9zc3KzP9+3bZ318/vx5HTt2TO7u7tbgv35DmKRsN5bdaNmyZWrYsKE++OAD69jRo0f14IMP3n1jAAC744g6H4wbN0579uzR1q1b9dFHH6lXr17q27evVq9erfnz5+vIkSOaN2+e1qxZk+1a8YoVKxQVFaWkpCS98cYbqlKliho3bqwKFSrovvvu0+zZs3X8+HEtWbJEGzZsuOm2XV1dtX//fu3evVvJycl69913tWfPnjzflAYAMCeCOh8EBARo4MCBGjZsmLp3764BAwbIy8tL77//vr788ksFBgZq8eLFmjx5spo0aWJdLigoSJGRkerWrZsuXryomTNnytnZWY6Ojho3bpx2796tgIAArVq1SoMGDbrptvv06SNvb2/17dtXoaGhOnnypIYMGaLExMR/qn0AgA05GIZh2LuIgiolJUWPPvqo1q1bp2rVquVp2T59+qhRo0Z68cUXbVTdnbNYLIqLi9OozaMUezTW3uUAgF15VvPUxuEb7bZ9jqgBADAxghoAABPjru+7UK1aNe3fv/+Oll24cGE+VwMAKIw4ogYAwMQIagAATOyOgvr8+fP6/PPPNXbsWJ05c0br16/XsWPH8rs2AACKvDwH9YEDB9SuXTstXrxYkZGRunjxoqKjo9W5c2e+QhEAgHyW56AeO3asevbsqSVLllg/6nL8+PEKDQ3V+++/n+8F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bUHq47obg9owrn2IRpcuXQwPDw/j8ccfN3755Zds8y9evNho1aqV4e3tbQwZMsQ4c+aMdVpmZqbx3//+12jQoIHRuHFjY8KECdZ9YwsHDhww+vbta3h7exvNmjUzpk6dat1eQerjzz//NF577TXD29vbaNKkSYHtwxYcDON/5xMAAIDpmPPCIwAAkERQAwBgagQ1AAAmRlADAGBiBDUAACZGUAMAYGIENQAAJkZQAyiyjh8/ro0bN9q7DOBvEdQAiqzXX39du3fvtncZwN8iqAEAMDGCGoApHD16VM8995x8fHzUunVrLViwQJKUlJSk5557Tr6+vmrRooWmTZumrKwsSdLUqVPVp0+fbOvx9/fXkiVLJEl9+vTRp59+queee06enp5q3769Nm/eLEkKCwtTTEyMpk2blmMdgJkQ1ADs7urVq3r22WdVqlQpLVq0SOHh4frwww+1bNkyhYaGqlKlSvr666/11ltv6bPPPrOGeG5Mnz5dnTp10sqVK/Xwww/rzTffVFZWlt544w35+Pjo2Wef1dSpU23YHXB3nO1dAAD8+OOPOnPmjP773//KxcVFtWvX1ujRo3Xu3DmVKFFCY8aMkbOzsx588EGlpaXp448/Vt++fXO17latWqlbt26SpOeff16dO3dWWlqaKleurGLFiqlkyZJydXW1XXPAXeKIGoDdJScny83NTS4uLtaxkJAQHT58WPXq1ZOz8/8fU/j4+CgtLU1//vlnrtZds2ZN6+Pr68/MzMyfwoF/AEENwO5uDOIbFS9ePMfY9evTFotFDg4OOab/NYSLFSuWYx6+3RcFCae+AdhdzZo1dfToUV2+fFklSpSQJL333nv64osvVKFCBWVkZFgDd9euXSpXrpxcXV1VrFgxXbx40bqeixcv6syZM3bpAbAVjqgB2F3z5s1VoUIFhYeHKykpSevWrVNkZKQmT56s9PR06/jatWs1depU9ezZUw4ODvLw8NC+ffv0/fffKzk5WeHh4XJ0zP2ftZIlS+rIkSP6/fffbdgdcHc4ogZgd87Ozvrkk0/0n//8R127dlWFChU0YsQItW3bVlWqVNG4cePUpUsXlStXTk8//bQGDhwoSWrSpIn69u1rDehnnnlGp06dyvV2u3fvrtdff139+vXT0qVLbdUecFccDC7WAABgWpz6BgDAxAhqAABMjKAGAMDECGoAAEyMoAYAwMQIagAATIygBgDAxAhqAABMjKAGAMDECGoAAEyMoAYAwMQIagAATOz/AOaLrsb6MMKeAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 500x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sb.catplot(y='Vote_Average',data = df, kind = 'count', color = 'green',order = df['Vote_Average'].value_counts().index)\n",
    "plt.title('Vote Distribution')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8bd6ae72-4849-4a26-a701-8cad56718d7e",
   "metadata": {},
   "source": [
    "What movie got the highest popularity ? What its genre?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "b32c737d-895e-4ba3-8a46-7c8ba96adc71",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Release_Date</th>\n",
       "      <th>Title</th>\n",
       "      <th>Popularity</th>\n",
       "      <th>Vote_Count</th>\n",
       "      <th>Vote_Average</th>\n",
       "      <th>Genre</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Action</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Adventure</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Release_Date                    Title  Popularity  Vote_Count Vote_Average  \\\n",
       "0          2021  Spider-Man: No Way Home    5083.954      8940.0      popular   \n",
       "1          2021  Spider-Man: No Way Home    5083.954      8940.0      popular   \n",
       "\n",
       "       Genre  \n",
       "0     Action  \n",
       "1  Adventure  "
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "cf5c9de4-1b2e-41be-81a5-74d861f57913",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Release_Date</th>\n",
       "      <th>Title</th>\n",
       "      <th>Popularity</th>\n",
       "      <th>Vote_Count</th>\n",
       "      <th>Vote_Average</th>\n",
       "      <th>Genre</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Action</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Adventure</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Science Fiction</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Release_Date                    Title  Popularity  Vote_Count Vote_Average  \\\n",
       "0          2021  Spider-Man: No Way Home    5083.954      8940.0      popular   \n",
       "1          2021  Spider-Man: No Way Home    5083.954      8940.0      popular   \n",
       "2          2021  Spider-Man: No Way Home    5083.954      8940.0      popular   \n",
       "\n",
       "             Genre  \n",
       "0           Action  \n",
       "1        Adventure  \n",
       "2  Science Fiction  "
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['Popularity'] == df['Popularity'].max()]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fa51bc7d-133d-4974-beca-344676b81f60",
   "metadata": {},
   "source": [
    "What movie got the lowest popularity ? What its genre?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "ac24d249-1d0d-4a28-9f34-d31450d41b72",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Release_Date</th>\n",
       "      <th>Title</th>\n",
       "      <th>Popularity</th>\n",
       "      <th>Vote_Count</th>\n",
       "      <th>Vote_Average</th>\n",
       "      <th>Genre</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Action</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Adventure</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>Spider-Man: No Way Home</td>\n",
       "      <td>5083.954</td>\n",
       "      <td>8940.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Science Fiction</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2022</td>\n",
       "      <td>The Batman</td>\n",
       "      <td>3827.658</td>\n",
       "      <td>1151.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Crime</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Release_Date                    Title  Popularity  Vote_Count Vote_Average  \\\n",
       "0          2021  Spider-Man: No Way Home    5083.954      8940.0      popular   \n",
       "1          2021  Spider-Man: No Way Home    5083.954      8940.0      popular   \n",
       "2          2021  Spider-Man: No Way Home    5083.954      8940.0      popular   \n",
       "3          2022               The Batman    3827.658      1151.0      popular   \n",
       "\n",
       "             Genre  \n",
       "0           Action  \n",
       "1        Adventure  \n",
       "2  Science Fiction  \n",
       "3            Crime  "
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "12e8f23d-9dde-4a5c-84e8-8ae8b72b3f15",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Release_Date</th>\n",
       "      <th>Title</th>\n",
       "      <th>Popularity</th>\n",
       "      <th>Vote_Count</th>\n",
       "      <th>Vote_Average</th>\n",
       "      <th>Genre</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>25545</th>\n",
       "      <td>2021</td>\n",
       "      <td>The United States vs. Billie Holiday</td>\n",
       "      <td>13.354</td>\n",
       "      <td>152.0</td>\n",
       "      <td>average</td>\n",
       "      <td>Music</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25546</th>\n",
       "      <td>2021</td>\n",
       "      <td>The United States vs. Billie Holiday</td>\n",
       "      <td>13.354</td>\n",
       "      <td>152.0</td>\n",
       "      <td>average</td>\n",
       "      <td>Drama</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25547</th>\n",
       "      <td>2021</td>\n",
       "      <td>The United States vs. Billie Holiday</td>\n",
       "      <td>13.354</td>\n",
       "      <td>152.0</td>\n",
       "      <td>average</td>\n",
       "      <td>History</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25548</th>\n",
       "      <td>1984</td>\n",
       "      <td>Threads</td>\n",
       "      <td>13.354</td>\n",
       "      <td>186.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>War</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25549</th>\n",
       "      <td>1984</td>\n",
       "      <td>Threads</td>\n",
       "      <td>13.354</td>\n",
       "      <td>186.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Drama</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25550</th>\n",
       "      <td>1984</td>\n",
       "      <td>Threads</td>\n",
       "      <td>13.354</td>\n",
       "      <td>186.0</td>\n",
       "      <td>popular</td>\n",
       "      <td>Science Fiction</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Release_Date                                 Title  Popularity  \\\n",
       "25545          2021  The United States vs. Billie Holiday      13.354   \n",
       "25546          2021  The United States vs. Billie Holiday      13.354   \n",
       "25547          2021  The United States vs. Billie Holiday      13.354   \n",
       "25548          1984                               Threads      13.354   \n",
       "25549          1984                               Threads      13.354   \n",
       "25550          1984                               Threads      13.354   \n",
       "\n",
       "       Vote_Count Vote_Average            Genre  \n",
       "25545       152.0      average            Music  \n",
       "25546       152.0      average            Drama  \n",
       "25547       152.0      average          History  \n",
       "25548       186.0      popular              War  \n",
       "25549       186.0      popular            Drama  \n",
       "25550       186.0      popular  Science Fiction  "
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['Popularity'] == df['Popularity'].min()]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db8f3717-7d40-4ae0-8c08-5bc709062318",
   "metadata": {},
   "source": [
    "Which year has the most filmmed movies?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "85b73c84-bddd-49b5-b769-c84c775f00b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjQAAAGxCAYAAAB1Hiz1AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/TGe4hAAAACXBIWXMAAA9hAAAPYQGoP6dpAABD80lEQVR4nO3dfVxUdd7/8TcMC4yWayqSiGutJQrCgCBa6XqzZt6WF5mVpZkW/lKzWy2kvCN182YtxRLK2/RK8yZbrauutVqrNTUpEHM1SFsJRaA0M4EROL8/vDjrCNaAo3jk9Xw8fDyY8znfM9/5MB7fnnPmjJdhGIYAAAAszLu2JwAAAHChCDQAAMDyCDQAAMDyCDQAAMDyCDQAAMDyCDQAAMDyCDQAAMDyCDQAAMDyCDQALMUq9wK9HOZ5OcwBuFQINICHDR06VCEhIS5/2rRpo/bt2ysuLk7vvPNOtbfZo0cPPfvssxdhthfHhg0bKvUgPDxcPXr00PPPP6+8vLxqb9PpdGrGjBnatGnTBc/v2WefrfT7iYyM1IABA5ScnKzi4mKX9YcOHaqhQ4e6vf20tDTFx8f/5noLFixQSEhIjZ/nfKrq1bPPPqsePXpc8LaBy5VPbU8AuBKFhoZq8uTJ5uOysjLl5eVp2bJlmjBhgho2bKiuXbvW4gwvjeTkZAUEBEiSioqKlJWVpdTUVG3ZskVr1qzRH/7wB7e3lZ+fr+XLl2vmzJkemVtAQICSk5MlSeXl5fr555+1a9cupaSk6LPPPtPy5cvl5+cnSS6/S3esXbtW33777W+ud9ddd6lLly7Vn/xvqKpXo0eP1rBhwzz+XMDlgkADXARXXXWVIiMjKy3/05/+pJtuukkbNmyoE4Gmbdu2Cg4ONh/fdNNN6tGjh+Li4jR58mQtXbq01ubm6+tb6XfUtWtXORwOjRkzRkuWLNEjjzwiSbrhhhsuyhyuvfZaXXvttRdl2+eqTngErIhTTsAl5OfnJ19fX3l5eZnLysvLlZqaqltvvVXt2rXTbbfdpjfeeONXt1NSUqJZs2apa9euateunQYMGKD33nvPZZ3i4mLNnTtXvXr1Urt27dS+fXs9+OCD+te//mWu8+OPP+qpp57SLbfcovDwcN1xxx3auHGjy3YOHz6sJ598UrGxsXI4HHrggQe0d+/eGvcgODhYd999t7Zt26ZDhw6Zy7ds2aIhQ4YoKipK7dq1U+/evbVq1SpJ0vfff68///nPkqSEhASXUye7du3S/fffL4fDodjYWD3zzDP68ccfazy/nj17KjIyUqtXrzaXnXsq6J///KcGDx6sqKgodejQQY888oh5RObZZ5/V22+/rdzcXIWEhGjDhg36/vvvFRISoqVLl6p3795yOBxav359pVNOFRYuXKibb75ZUVFRGj16tHJycsxaVaeOKrZf8VxV9erccWVlZVq1apUGDBigiIgIdevWTXPmzFFJSYnLcw0fPlzr16/Xbbfdpnbt2umOO+7QJ598UuP+AhcLgQa4CAzDUGlpqfmnpKREBw4cUEJCgn755Rfdcccd5rpTpkzR/Pnzdfvtt2vRokXq3bu3ZsyYoYULF55322PGjNHq1av14IMP6tVXX1VUVJSeeOIJlzAyYcIErV+/XvHx8VqyZIkSEhKUlZWlp556yrxYdPz48fr22281depUvfbaawoNDdUzzzyj7du3SzoTeO655x59/fXXev755zV37lyVl5frvvvuc+uUyvnccsstks5cayJJ//jHPzRmzBiFhYXplVde0YIFC9SiRQtNmzZNGRkZatq0qXl66JFHHjF//uKLLzR8+HD5+/vrpZde0sSJE7Vz504NGzas0nUw1Z1fXl6ecnNzK9VycnI0evRotWvXTq+++qqmT5+ugwcPKj4+XuXl5Ro9erS6du2qgIAArVmzRt26dTPHLliwQA8//LBmzZpl9uBcaWlpevfddzVp0iS98MIL2rdvn4YNG6aTJ0+6Nffz9epckyZN0syZM9WzZ0+9+uqruu+++7Ry5UqNHj3a5WLiPXv2aPHixRo3bpwWLlwom82mRx99VD/99JNb8wEuFU45ARfBF198obCwMJdlXl5eat26tV5++WV1795dknTw4EG99dZbevLJJ82LSDt37iwvLy+lpKRoyJAhuuaaa1y2s23bNn366aeaN2+e+vbtK0nq0qWLioqKNGfOHPXv31/l5eX65Zdf9Nxzz5nrxMbG6uTJk/rLX/6iwsJCBQQEaOfOnRozZox69uxprtOwYUP5+vpKkpYvX67jx4/rzTffVPPmzSWdOW3Wt29fvfzyy5o/f36N+lNxXU1BQYEkKTs7W//1X/+lxMREc52oqCh17NhRO3bskMPhUNu2bSWdOXUSGhoqSZo7d66uv/56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qnp1thtuuEH/9V//pfnz56uoqEgdOnTQv/71LyUnJ6tjx44X5WZ/wMVGoAEuoT/+8Y8aOnSolixZojfffFP333+/Zs6cqZSUFK1evVp5eXlq3Lix+vbtq8cff7zK/2l7e3srNTVVL7/8slJSUvTDDz8oMDBQDz74oMaMGSPpzGmnuXPnKjk5WY888oh+//vfKzIyUm+88YaGDh2qXbt2KSQkRMnJyfrrX/+ql19+WceOHVOzZs00duxY85MvgYGBWr16tebOnaspU6aopKRE1113naZPn65Bgwb95usdO3as+fPvfvc7NW/eXLfeeqvi4+Ndrt/4y1/+oqSkJPNIx3XXXaepU6fqb3/7m3bt2iXpzBGZBx98UGvWrNHWrVv1z3/+U507d9bixYuVnJyscePG6Xe/+53CwsK0dOnSKm9seLaCggLdfffd5uN69erp+uuv17hx4zR06FD97ne/q3JcmzZttGjRIi1cuFBPPvmkysrK1K5dOy1ZssS84DsuLk5bt27VmDFjNG7cOPOTZu7o2bOngoKCNH78eJWWlqp79+5KTEw0rwm65ZZb9Mwzz+iNN97QBx98oLCwMCUnJ+uee+4xt1FVr841ffp0tWzZUuvXr9drr72mpk2batiwYRo9evQFHWECaouXwbeXAQAAiyOGAwAAyyPQAAAAyyPQAAAAyyPQAAAAyyPQAAAAyyPQAAAAy6vxfWicTqfi4uL0/PPPq2PHji61n3/+WX379tUTTzyhuLg4c/nmzZv10ksvqaCgQJ07d1ZSUpL5nTaGYWju3Llat26dysvLNWjQID399NPm/RCOHTumSZMm6bPPPtM111yjxx57THfccYdbcy0vL1dpaam8vb1/9XtWAADA5cMwDJWXl8vHx+c3749Uo0BTUlKip556SllZWVXWZ8+erfz8fJdlu3fvVmJioqZOnao2bdpo+vTpSkhIUEpKiiRp6dKl2rx5s5KTk1VaWqrx48ercePGGjlypCQpISFBxcXFWrNmjTIyMvTcc8/p+uuvd+sbbktLS81v7gUAANYSHh7+m98dV+1Ak52draeeeuq834C7a9cubd++vdK3uK5cuVJ9+vTRwIEDJUmzZs1S9+7dlZOToxYtWmjFihUaN26cy5fVvfzyyxo5cqQOHTqkjz/+WB9++KGCg4PVunVrpaen67//+7/dCjQVqS48PLxG3z1TVlamzMzMGo+vS+iV++iV++iV++iV++iV+2qrVxXP687dq6sdaHbu3KmOHTvqiSeeqHRrcafTqeeff16TJk1y+Z4W6cwXrD388MPm42bNmikoKEgZGRny9fXVkSNH1KFDB7MeHR2t3Nxc5efnKyMjQ82aNVNwcLBLveLozm+pOM1ks9ku6BdxoePrEnrlPnrlPnrlPnrlPnrlvtrqlTuXi1Q70AwZMuS8tUWLFik0NFSdO3euVMvPz1fTpk1dljVu3Fh5eXkqKCiQJJd6kyZNJMmsVzX26NGj1Zp7WVlZtdY/d1xNx9cl9Mp99Mp99Mp99Mp99Mp9tdWr6jyfx76cMjs7W6tXr9bf/va3KuvFxcWVzn/5+vrK6XSquLjYfHx2TTpz1KeoqOi8Y6vjQq+j4Toc99Er99Er99Er99Er99Er913OvfJIoDEMQ88995zGjRtnHlk5l5+fX6UA4nQ6ZbfbXcJLxTfKVqxrt9vPO9bf379a8+QamouPXrmPXrmPXrmPXrmPXrmvtq+hcYdHAs3hw4f11Vdfaf/+/XrxxRclSUVFRZo8ebLee+89vf766woMDFRhYaHLuMLCQgUEBCgwMFCSVFBQYF4nU3EaqqJ+vrHVwTU0lw69ch+9ch+9ch+9ch+9ct/l3CuPBJrAwED97//+r8uyoUOHaujQobr99tslSQ6HQ2lpaeZ9aY4cOaIjR47I4XAoMDBQQUFBSktLMwNNWlqagoKC1LRpU0VGRio3N1d5eXm69tprzfq5FyUDAIC6ySOBxsfHRy1btqy0rHHjxubRl3vvvVdDhw5VZGSkwsPDNX36dHXr1k0tWrQw63PmzDEDy9y5czVixAhJUosWLdS5c2eNHz9eiYmJyszM1ObNm7Vy5UpPTB8AAFicxy4K/i1RUVGaNm2a5s+fr59++km33HKLkpKSzPrIkSP1ww8/aOzYsbLZbBo0aJCGDx9u1mfNmqXExEQNHjxYAQEBmjFjhlv3oAEAAFe+Cwo0+/fvP2/to48+qrQsLi7O5asQzmaz2ZSQkKCEhIQq640bN9aiRYtqNlEAAHBF48spAQCA5RFoAACA5RFoAACA5RFoAACA5RFoAACA5RFoAADAb7Lb7bU9hV9FoAEA4DJTVm7U9hRc2Gw2hYaG/urXHtT2nC/ZjfUAAIB7bN5eemz1V8rOP1nbU3HLDU2v0sv3RNXqHAg0AABchrLzT+rrwydqexqWwSknAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeQQaAABgeTUONE6nU/3799eOHTvMZenp6brnnnsUFRWl2267TWvXrnUZs23bNvXv318Oh0PDhg1TTk6OS33ZsmXq0qWLoqKiNHHiRBUVFZm1kpISTZw4UTExMercubOWLFlS06kDAIArTI0CTUlJiZ588kllZWWZywoKCvTwww8rNjZWb7/9tsaNG6ekpCT94x//kCQdPnxYY8aMUVxcnNatW6dGjRpp9OjRMgxDkvTBBx8oOTlZ06ZN0/Lly5WRkaHZs2eb2581a5b27Nmj5cuXa/LkyUpOTtb7779/AS8dAABcKaodaLKzszV48GAdOnTIZfmWLVvUpEkTPfnkk7ruuuvUr18/DRw4UJs2bZIkrV27Vu3atdOIESN04403aubMmcrNzdXOnTslSStWrNADDzyg7t27KyIiQlOnTtX69etVVFSkU6dOae3atUpMTFRYWJhuvfVWPfTQQ1q1apUHWgAAAKyu2oFm586d6tixo9asWeOyvEuXLpo5c2al9U+ePClJysjIUExMjLncbrcrLCxM6enpKisrU2Zmpks9MjJSp0+f1r59+7Rv3z6VlpYqKirKrEdHRysjI0Pl5eXVfQkAAOAK41PdAUOGDKlyeXBwsIKDg83HP/zwg9599109+uijks6ckmratKnLmMaNGysvL08nTpxQSUmJS93Hx0cNGzZUXl6evL29dc0118jX19esN2nSRCUlJTp+/LgaNWrk1tzLysrcfp1Vjavp+LqEXrmPXrmPXrmPXrnvcu6VzWar7SnUiKd7WZ3tVTvQuKO4uFiPPvqomjRporvvvluSVFRU5BJIJMnX11dOp1PFxcXm46rqhmFUWZPOXJzsrszMzGq/Fk+Or0volfvolfvolfvolfsut17Z7XaFhobW9jRqZP/+/S4f6LmUPB5ofvnl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ZcoUDR48WHa7XXa7XQMHDtSUKVO0e/dubdmyRUuWLNGwYcM8NX0AAGBhHjvlZLPZ9MorrygxMVFxcXFq2bKlFi5cqKCgIElScHCwFixYoBkzZmjhwoWKiorSwoUL5eXlJUnq16+fcnNzNWnSJDmdTvXq1Uvjx483t5+QkKApU6bogQce0FVXXaVHH31UvXr18tT0AQCAhV1QoNm/f7/L45YtW2rlypXnXb9r167q2rXreevx8fGKj4+vsma32/Xiiy/qxRdfrNlkAQDAFYsLUAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOURaAAAgOV5NNAcOXJEo0aNUvv27dWjRw8tW7bMrO3du1d33XWXHA6H7rzzTu3Zs8dl7ObNm9WzZ085HA6NGTNGP/74o1kzDENz5sxRp06dFBsbq1mzZqm8vNyTUwcAABbm0UDz+OOPq169etqwYYMmTpyol156SX//+9916tQpxcfHKyYmRhs2bFBUVJRGjRqlU6dOSZJ2796txMREjR07VmvWrNGJEyeUkJBgbnfp0qXavHmzkpOTNX/+fG3atElLly715NQBAICFeSzQ/PTTT0pPT9cjjzyi6667Tj179lSXLl30+eef67333pOfn58mTJigVq1aKTExUfXr19f7778vSVq5cqX69OmjgQMHqk2bNpo1a5a2bt2qnJwcSdKKFSs0btw4xcTEqFOnTnr66ae1atUqT00dAABYnI+nNuTv7y+73a4NGzboqaeeUk5Ojr788ks9/vjjysjIUHR0tLy8vCRJXl5eat++vdLT0xUXF6eMjAw9/PDD5raaNWumoKAgZWRkyNfXV0eOHFGHDh3MenR0tHJzc5Wfn6+mTZu6PceysrIavbaKcTUdX5fQK/fRK/fRK/fRK/ddzr2y2Wy1PYUa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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['Release_Date'].hist()\n",
    "plt.title('Release Date Distribution')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ec9db0e-723a-4efb-9dfe-5df1d77302ca",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

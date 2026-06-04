import plotly.express as px

def score_distribution(df):
    fig = px.histogram(
        df,
        x="exam_score",
        nbins=30,
        title="Exam Score Distribution"
    )
    return fig


def study_vs_score(df):
    fig = px.scatter(
        df,
        x="study_hours",
        y="exam_score",
        color="placement_status",
        title="Study Hours vs Exam Score"
    )
    return fig


def attendance_vs_score(df):
    fig = px.scatter(
        df,
        x="attendance",
        y="exam_score",
        color="placement_status",
        title="Attendance vs Exam Score"
    )
    return fig


def sleep_vs_score(df):
    fig = px.scatter(
        df,
        x="sleep_hours",
        y="exam_score",
        color="placement_status",
        title="Sleep Hours vs Exam Score"
    )
    return fig

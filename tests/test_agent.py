from jobseekeragent.agent import CandidateProfile, JobPosting, JobSeekerAgent


def _profile() -> CandidateProfile:
    return CandidateProfile(
        name="Jordan",
        skills={"python", "sql", "docker"},
        preferred_locations={"Remote"},
        target_titles={"Data Engineer"},
    )


def test_evaluate_calculates_skill_and_preference_bonuses() -> None:
    agent = JobSeekerAgent(_profile())
    posting = JobPosting(
        title="Data Engineer",
        location="Remote",
        required_skills={"python", "sql", "airflow"},
        description="desc",
    )

    result = agent.evaluate(posting)

    assert result.matched_skills == {"python", "sql"}
    assert result.missing_skills == {"airflow"}
    assert result.title_match is True
    assert result.location_match is True
    assert result.score == 0.967


def test_rank_orders_by_score_descending() -> None:
    agent = JobSeekerAgent(_profile())
    high = JobPosting(
        title="Data Engineer",
        location="Remote",
        required_skills={"python"},
        description="desc",
    )
    low = JobPosting(
        title="Site Reliability Engineer",
        location="Onsite",
        required_skills={"go", "kubernetes"},
        description="desc",
    )

    ranked = agent.rank([low, high])

    assert [r.posting.title for r in ranked] == ["Data Engineer", "Site Reliability Engineer"]

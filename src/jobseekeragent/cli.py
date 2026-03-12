from __future__ import annotations

from .agent import CandidateProfile, JobPosting, JobSeekerAgent


def demo() -> str:
    profile = CandidateProfile(
        name="Alex",
        skills={"python", "sql", "docker", "aws"},
        preferred_locations={"Remote", "Berlin"},
        target_titles={"Data Engineer", "Backend Engineer"},
    )

    postings = [
        JobPosting(
            title="Senior Data Engineer",
            location="Remote",
            required_skills={"python", "sql", "airflow"},
            description="Build and scale data pipelines",
        ),
        JobPosting(
            title="Backend Engineer",
            location="Munich",
            required_skills={"python", "docker", "kubernetes"},
            description="Develop APIs and platform services",
        ),
    ]

    agent = JobSeekerAgent(profile)
    ranked = agent.rank(postings)

    lines = [f"Top matches for {profile.name}:"]
    for result in ranked:
        lines.append(
            f"- {result.posting.title} ({result.posting.location}) => {result.score:.2f}"
        )

    return "\n".join(lines)


if __name__ == "__main__":
    print(demo())

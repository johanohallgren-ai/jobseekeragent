from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CandidateProfile:
    name: str
    skills: set[str]
    preferred_locations: set[str]
    target_titles: set[str]


@dataclass(slots=True)
class JobPosting:
    title: str
    location: str
    required_skills: set[str]
    description: str


@dataclass(slots=True)
class JobMatchResult:
    posting: JobPosting
    score: float
    matched_skills: set[str]
    missing_skills: set[str]
    title_match: bool
    location_match: bool


class JobSeekerAgent:
    """Scores job postings against a candidate profile and ranks the results."""

    def __init__(self, profile: CandidateProfile) -> None:
        self.profile = profile

    def evaluate(self, posting: JobPosting) -> JobMatchResult:
        matched_skills = self.profile.skills & posting.required_skills
        missing_skills = posting.required_skills - self.profile.skills

        skill_score = (
            len(matched_skills) / len(posting.required_skills)
            if posting.required_skills
            else 1.0
        )
        title_match = any(
            target.lower() in posting.title.lower()
            for target in self.profile.target_titles
        )
        location_match = posting.location in self.profile.preferred_locations

        title_bonus = 0.2 if title_match else 0.0
        location_bonus = 0.1 if location_match else 0.0
        score = min(skill_score + title_bonus + location_bonus, 1.0)

        return JobMatchResult(
            posting=posting,
            score=round(score, 3),
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            title_match=title_match,
            location_match=location_match,
        )

    def rank(self, postings: list[JobPosting]) -> list[JobMatchResult]:
        """Return postings sorted by descending score and title."""
        results = [self.evaluate(posting) for posting in postings]
        return sorted(results, key=lambda result: (-result.score, result.posting.title))

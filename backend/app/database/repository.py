from app.database.db import get_connection, release_connection


def save_audit(
    url,
    cri,
    dom,
    fact,
    entity,
    tone,
    retrieval,
    section_breakdown,
):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO audits
            (url, cri_score, dom_score, fact_score, entity_score, tone_score, retrieval_score)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id
            """,
            (url, cri, dom, fact, entity, tone, retrieval),
        )

        audit_id = cursor.fetchone()[0]

        for section in section_breakdown:
            cursor.execute(
                """
                INSERT INTO sections
                (audit_id, heading, fact_score, entity_score, tone_score, retrieval_score)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    audit_id,
                    section["heading"],
                    section["fact_density"],
                    section["entity_clarity"],
                    section["tone_neutrality"],
                    retrieval,
                ),
            )

        conn.commit()
        return audit_id

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        cursor.close()
        release_connection(conn)

CREATE TABLE IF NOT EXISTS public.artist
(
    artist text COLLATE pg_catalog."default" NOT NULL,
    title text COLLATE pg_catalog."default" NOT NULL,
    recommendation_id text COLLATE pg_catalog."default" NOT NULL,
    "timestamp" text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT artist_pkey PRIMARY KEY (recommendation_id)
)
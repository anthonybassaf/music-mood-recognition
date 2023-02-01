CREATE TABLE IF NOT EXISTS public.artist_table
(
    dzr_sng_id bigint NOT NULL,
    "TrackId" text COLLATE pg_catalog."default" NOT NULL,
    valence double precision NOT NULL,
    arousal double precision NOT NULL,
    "ArtistName" text COLLATE pg_catalog."default" NOT NULL,
    "Title" text COLLATE pg_catalog."default" NOT NULL,
    "Lyrics" text COLLATE pg_catalog."default" NOT NULL,
    label double precision NOT NULL,
    "Mood" text COLLATE pg_catalog."default" NOT NULL
);

CREATE TABLE IF NOT EXISTS public.artist
(
    artist text COLLATE pg_catalog."default" NOT NULL,
    title text COLLATE pg_catalog."default" NOT NULL,
    recommendation_id text COLLATE pg_catalog."default" NOT NULL,
    "timestamp" text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT artist_pkey PRIMARY KEY (recommendation_id)
);

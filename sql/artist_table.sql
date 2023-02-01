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
)
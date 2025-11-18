-- prepare_similarity_search_service_db.sql

-- Create the database for the similarity search service
CREATE DATABASE similarity_search_service_db;

-- Connect to the database
\connect similarity_search_service_db;

-- Enable vectorscale extension
CREATE EXTENSION IF NOT EXISTS vectorscale CASCADE;
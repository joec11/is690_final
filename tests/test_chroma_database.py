"""Test chroma_database.py"""
import os
import shutil

def test_create_and_delete_chroma_directory():
    """Test creating and deleting the chroma directory."""
    chroma_path = "test_chroma"

    # Test create chroma directory
    if os.path.exists(chroma_path): \
        shutil.rmtree(chroma_path)

    os.makedirs(chroma_path)
    assert os.path.exists(chroma_path)

    # Test delete chroma directory
    shutil.rmtree(chroma_path)
    assert not os.path.exists(chroma_path)
